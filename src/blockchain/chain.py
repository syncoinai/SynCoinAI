import time
from blockchain.block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.tx_counter = 0  # contador de transacciones

    def create_genesis_block(self):
        return Block(
            index=0,
            previous_hash="0",
            transactions=[],
            ai_data={"info": "Genesis Block"},
            ia_proof="genesis_proof"
        )

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, from_node, to_node, data, data_type="generic"):
        """
        Agrega una transacción pendiente con estructura mejorada
        """
        self.tx_counter += 1
        tx_id = f"tx{self.tx_counter}"
        timestamp = time.time()
        transaction = {
            "tx_id": tx_id,
            "timestamp": timestamp,
            "from_node": from_node,
            "to_node": to_node,
            "data_type": data_type,
            "data": data
        }
        self.pending_transactions.append(transaction)
        return tx_id

    def mine_block(self, ia_proof, ai_data=None):
        """
        Crea un bloque con las transacciones pendientes y prueba de IA
        """
        if not ia_proof:
            raise ValueError("IA proof is required to mine a block.")

        block = Block(
            index=len(self.chain),
            previous_hash=self.get_last_block().hash,
            transactions=self.pending_transactions,
            ai_data=ai_data,
            ia_proof=ia_proof
        )
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def is_valid(self):
        """
        Verifica integridad de la blockchain
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
            if not current.ia_proof:
                return False
        return True

    def get_all_transactions(self):
        """
        Devuelve todas las transacciones de todos los bloques
        """
        all_txs = []
        for block in self.chain:
            all_txs.extend(block.transactions)
        return all_txs

    def __repr__(self):
        return "\n".join(str(block) for block in self.chain)
