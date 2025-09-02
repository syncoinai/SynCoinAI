import time
import hashlib
import json
from decimal import Decimal, getcontext
from .block import Block

# precisión alta para decimales (18 decimales como ETH)
getcontext().prec = 50

# Parámetros token
DECIMALS = 18
UNIT = 10 ** DECIMALS
TOTAL_SUPPLY_SYNC = 21_000_000
TOTAL_SUPPLY_ATTO = TOTAL_SUPPLY_SYNC * UNIT

INITIAL_REWARD_SYNC = 20
INITIAL_REWARD_ATTO = INITIAL_REWARD_SYNC * UNIT

DEFAULT_TARGET_BLOCK_TIME_SECONDS = 10
HALVING_YEARS = 2
BLOCKS_PER_HALVING = int((HALVING_YEARS * 365 * 24 * 3600) / DEFAULT_TARGET_BLOCK_TIME_SECONDS)

# Tarifa mínima
MIN_FEE_SYNC = Decimal("1e-12")
MIN_FEE_ATTO = int((MIN_FEE_SYNC * Decimal(UNIT)).to_integral_value())


class Blockchain:
    def __init__(self,
                 mining_reward_atto=INITIAL_REWARD_ATTO,
                 blocks_per_halving=BLOCKS_PER_HALVING,
                 target_block_time_seconds=DEFAULT_TARGET_BLOCK_TIME_SECONDS):
        self.chain = []
        self.pending_transactions = []   # mempool
        self.balances = {}               # node_id -> attoSYNC
        self.total_minted = 0
        self.mining_reward_atto = mining_reward_atto
        self.blocks_per_halving = blocks_per_halving
        self.target_block_time_seconds = target_block_time_seconds

        # índices
        self.tx_index = {}               # tx_id -> tx
        self.contracts = {}              # contract_id -> contract_data

        self.create_genesis_block()

    # ---------- GENESIS ----------
    def create_genesis_block(self):
        genesis = Block(
            index=0,
            previous_hash="0",
            ia_proof="genesis_proof",
            transactions=[],
            ai_data={"info": "Genesis Block"},
            nonce=0,
            timestamp=time.time()
        )
        self.chain.append(genesis)
        return genesis

    def get_last_block(self):
        return self.chain[-1]

    # ---------- conversion utils ----------
    @staticmethod
    def sync_to_atto(amount_sync):
        return int((Decimal(str(amount_sync)) * Decimal(UNIT)).to_integral_value())

    @staticmethod
    def atto_to_sync_str(amount_atto):
        a = Decimal(amount_atto) / Decimal(UNIT)
        return format(a.normalize(), 'f')

    # ---------- rewards ----------
    def current_block_reward(self, height):
        halvings = height // self.blocks_per_halving
        reward_dec = Decimal(self.mining_reward_atto) / (Decimal(2) ** halvings)
        reward_atto = int(reward_dec.to_integral_value(rounding="ROUND_FLOOR"))
        remaining = TOTAL_SUPPLY_ATTO - self.total_minted
        if remaining <= 0:
            return 0
        return min(reward_atto, remaining)

    # ---------- tx management ----------
    def add_transaction(self, tx):
        """
        tx debe ser un dict ya formado con campos básicos:
        {
          "tx_id", "from_node", "to_node", "amount_atto", "fee_atto",
          "signatures": [...], "required_signatures": int, "data_type", "data"
        }
        """
        # verificar fondos (si no es SYSTEM)
        if tx.get("from_node") != "SYSTEM":
            total_out = tx.get("amount_atto", 0) + tx.get("fee_atto", 0)
            if total_out > self.balances.get(tx["from_node"], 0):
                print(f"[ERROR] {tx['from_node']} saldo insuficiente.")
                return None

        # verificar multifirmas (si aplica)
        if tx.get("required_signatures"):
            if len(tx.get("signatures", [])) < tx["required_signatures"]:
                print(f"[ERROR] Transacción {tx['tx_id']} no cumple firmas requeridas.")
                return None

        self.pending_transactions.append(tx)
        self.tx_index[tx["tx_id"]] = tx
        return tx["tx_id"]

    # ---------- minado ----------
    def mine_block(self, ia_proof, miner_node, ai_data=None):
        if not self.pending_transactions and self.current_block_reward(len(self.chain)) == 0:
            print("Nada que minar.")
            return None

        reward_atto = self.current_block_reward(len(self.chain))
        total_fees = sum(tx.get("fee_atto", 0) for tx in self.pending_transactions)

        # copiar txs + añadir reward
        block_txs = list(self.pending_transactions)
        if reward_atto > 0:
            reward_tx = {
                "tx_id": hashlib.sha256(f"reward-{time.time()}-{miner_node}".encode()).hexdigest()[:16],
                "timestamp": time.time(),
                "from_node": "SYSTEM",
                "to_node": miner_node,
                "amount_atto": reward_atto,
                "data_type": "reward",
                "data": "block_reward",
                "fee_atto": 0
            }
            block_txs.append(reward_tx)
            self.total_minted += reward_atto
            self.tx_index[reward_tx["tx_id"]] = reward_tx

        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_last_block().hash,
            ia_proof=ia_proof,
            transactions=block_txs,
            ai_data=ai_data or {},
            nonce=0
        )

        # simple PoW (1 zero)
        while not new_block.hash.startswith("0"):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        # aplicar estado
        self.chain.append(new_block)
        self._apply_transactions(new_block.transactions, miner_node)

        # limpiar mempool
        self.pending_transactions = []

        print(f"Bloque {new_block.index} minado -> reward {self.atto_to_sync_str(reward_atto)} SYNC, fees {self.atto_to_sync_str(total_fees)} SYNC")
        return new_block

    def _apply_transactions(self, transactions, miner_node):
        total_fees = 0
        for tx in transactions:
            fee = tx.get("fee_atto", 0)
            total_fees += fee
            sender = tx.get("from_node")
            to = tx.get("to_node")
            amt = tx.get("amount_atto", 0)

            # transfer normal
            if amt > 0 and to:
                if sender != "SYSTEM":
                    self.balances[sender] = self.balances.get(sender, 0) - amt - fee
                self.balances[to] = self.balances.get(to, 0) + amt
            else:
                if sender != "SYSTEM":
                    self.balances[sender] = self.balances.get(sender, 0) - fee

            # contract call (simplificado)
            if tx.get("data_type") == "contract_call":
                cid = tx["data"].get("contract_id")
                code = tx["data"].get("contract_code")
                self.contracts[cid] = code

        if total_fees > 0:
            self.balances[miner_node] = self.balances.get(miner_node, 0) + total_fees

    # ---------- consultas ----------
    def get_balance(self, node_id):
        return self.balances.get(node_id, 0)

    def get_balance_sync_str(self, node_id):
        return self.atto_to_sync_str(self.get_balance(node_id))

    def get_balance_at(self, node_id, height):
        if height >= len(self.chain):
            return self.get_balance(node_id)
        balance = 0
        for block in self.chain[:height+1]:
            for tx in block.transactions:
                if tx.get("to_node") == node_id:
                    balance += tx.get("amount_atto", 0)
                if tx.get("from_node") == node_id and tx.get("from_node") != "SYSTEM":
                    balance -= tx.get("amount_atto", 0) + tx.get("fee_atto", 0)
        return balance

    def get_block_by_height(self, height):
        if 0 <= height < len(self.chain):
            return self.chain[height]
        return None

    def get_block_by_hash(self, h):
        return next((b for b in self.chain if b.hash == h), None)

    def get_transaction(self, tx_id):
        return self.tx_index.get(tx_id)

    def get_all_transactions(self):
        all_txs = []
        for block in self.chain:
            all_txs.extend(block.transactions)
        return all_txs

    # ---------- validez y rollback ----------
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i - 1]
            if cur.hash != cur.calculate_hash():
                print(f"Invalid hash at block {cur.index}")
                return False
            if cur.previous_hash != prev.hash:
                print(f"Broken link at block {cur.index}")
                return False
        return True

    def rollback(self, n=1):
        if n >= len(self.chain):
            raise ValueError("No puedes eliminar el bloque génesis")
        for _ in range(n):
            removed = self.chain.pop()
            print(f"Rollback -> eliminado bloque {removed.index}")
        # ⚠ estado no recalculado aquí (puede añadirse un recalculo completo)

    # ---------- persistencia ----------
    def export_chain(self, filepath):
        data = [b.to_dict() for b in self.chain]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def import_chain(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.chain = [Block(**blk) for blk in data]
