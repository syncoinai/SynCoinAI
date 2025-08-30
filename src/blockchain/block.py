import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions=None, ai_data=None, ia_proof=None, timestamp=None):
        """
        index: número del bloque
        previous_hash: hash del bloque anterior
        transactions: lista de transacciones (entre IA o financieras)
        ai_data: diccionario con información relevante de IA
        ia_proof: hash generado por la IA como prueba
        timestamp: tiempo de creación
        """
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions or []
        self.ai_data = ai_data or {}
        self.ia_proof = ia_proof  # hash único generado por la IA
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calcula el hash SHA256 del bloque combinando todos sus campos
        """
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "ai_data": self.ai_data,
            "ia_proof": self.ia_proof,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:10]}..., prev={self.previous_hash[:10]}..., ia_proof={str(self.ia_proof)[:10]}...)"

