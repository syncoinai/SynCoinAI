import time
import hashlib
import json

def calculate_merkle_root(transactions):
    """
    Calcula un Merkle Root simple a partir de las transacciones.
    Cada transacción debe ser un dict serializable.
    """
    if not transactions:
        return ""
    hashes = [hashlib.sha256(json.dumps(tx, sort_keys=True, default=str).encode()).hexdigest() for tx in transactions]
    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else left
            temp.append(hashlib.sha256((left + right).encode()).hexdigest())
        hashes = temp
    return hashes[0]

class Block:
    """
    Block(index, previous_hash, ia_proof, transactions, ai_data=None, nonce=0, timestamp=None)
    - transactions: lista serializable de transacciones (dicts)
    - ai_data: dict con metadatos IA (tipo de datos, versión de modelo, etc.)
    - nonce: entero para PoW (si se implementa)
    """
    def __init__(self, index, previous_hash, ia_proof, transactions=None, ai_data=None, nonce=0, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.ia_proof = ia_proof
        self.transactions = transactions or []
        self.ai_data = ai_data or {}
        self.nonce = nonce
        self.merkle_root = calculate_merkle_root(self.transactions)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Hash determinista que incluye nonce, timestamp, ia_proof, transactions, ai_data y merkle_root.
        """
        block_content = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "ia_proof": self.ia_proof,
            "nonce": self.nonce,
            "transactions": self.transactions,
            "ai_data": self.ai_data,
            "merkle_root": self.merkle_root
        }
        block_string = json.dumps(block_content, sort_keys=True, default=str)
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()

    def update_transactions(self, new_transactions):
        """
        Reemplaza las transacciones y recalcula el Merkle root y el hash.
        Útil para añadir un batch de transacciones antes de minar.
        """
        self.transactions = new_transactions
        self.merkle_root = calculate_merkle_root(self.transactions)
        self.hash = self.calculate_hash()

    def verify_block_integrity(self):
        """
        Verifica que el hash coincida con el contenido actual y que Merkle root sea correcto.
        """
        correct_merkle = calculate_merkle_root(self.transactions)
        if self.merkle_root != correct_merkle:
            return False
        return self.hash == self.calculate_hash()

    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "ia_proof": self.ia_proof,
            "nonce": self.nonce,
            "transactions": self.transactions,
            "ai_data": self.ai_data,
            "merkle_root": self.merkle_root,
            "hash": self.hash
        }

    def __repr__(self):
        return (f"Block(index={self.index}, hash={self.hash[:12]}..., "
                f"prev={self.previous_hash[:12]}..., nonce={self.nonce}, "
                f"txs={len(self.transactions)})")
