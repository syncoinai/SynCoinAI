import time
import hashlib
from decimal import Decimal, getcontext
from .block import Block

# precisión para decimales (suficiente para 18 decimales)
getcontext().prec = 50

# Parámetros token
DECIMALS = 18
UNIT = 10 ** DECIMALS                       # 1 SYNC = 1e18 attoSYNC
TOTAL_SUPPLY_SYNC = 21_000_000
TOTAL_SUPPLY_ATTO = TOTAL_SUPPLY_SYNC * UNIT

INITIAL_REWARD_SYNC = 20                    # 20 SYNC inicial
INITIAL_REWARD_ATTO = INITIAL_REWARD_SYNC * UNIT

# Halving ≈ cada 2 años (ajustable)
DEFAULT_TARGET_BLOCK_TIME_SECONDS = 10      # ejemplo: 10s por bloque (ajusta si cambia)
HALVING_YEARS = 2
BLOCKS_PER_HALVING = int((HALVING_YEARS * 365 * 24 * 3600) / DEFAULT_TARGET_BLOCK_TIME_SECONDS)

# Tarifa mínima (ejemplo 1e-12 SYNC)
MIN_FEE_SYNC = Decimal("1e-12")
MIN_FEE_ATTO = int((MIN_FEE_SYNC * Decimal(UNIT)).to_integral_value())

class Blockchain:
    def __init__(self,
                 mining_reward_atto=INITIAL_REWARD_ATTO,
                 blocks_per_halving=BLOCKS_PER_HALVING,
                 target_block_time_seconds=DEFAULT_TARGET_BLOCK_TIME_SECONDS):
        self.chain = []
        self.pending_transactions = []   # mempool
        self.balances = {}               # node_id -> atto (int)
        self.total_minted = 0            # attoSYNC minted via rewards
        self.mining_reward_atto = mining_reward_atto
        self.blocks_per_halving = blocks_per_halving
        self.target_block_time_seconds = target_block_time_seconds
        self.create_genesis_block()

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

    # ---------- utilidades de cantidad ----------
    @staticmethod
    def sync_to_atto(amount_sync):
        """
        amount_sync: str/Decimal/float representing SYNC units
        devuelve entero attoSYNC
        """
        a = Decimal(str(amount_sync))
        return int((a * Decimal(10) ** DECIMALS).to_integral_value())

    @staticmethod
    def atto_to_sync_str(amount_atto):
        a = Decimal(amount_atto) / Decimal(10) ** DECIMALS
        # formatear sin notación exponencial
        s = format(a.normalize(), 'f')
        return s

    # ---------- recompensa actual ----------
    def current_block_reward(self, height):
        halvings = height // self.blocks_per_halving
        # recompensa en atto (flotante Decimal -> entero)
        reward_dec = Decimal(self.mining_reward_atto) / (Decimal(2) ** halvings)
        reward_atto = int(reward_dec.to_integral_value(rounding="ROUND_FLOOR"))
        remaining = TOTAL_SUPPLY_ATTO - self.total_minted
        if remaining <= 0:
            return 0
        if reward_atto > remaining:
            return remaining
        return reward_atto

    # ---------- añadir transacción ----------
    def add_transaction(self, from_node, to_node=None, data_type="generic", data=None,
                        amount_sync=0, fee_sync=None, batch=None):
        """
        Añade tx al mempool.
        - Si batch (lista de subtransfers): cada item {'to_node','amount_sync','data_type','data'}
        - fee_sync: en SYNC; si None se usa MIN_FEE_SYNC
        Devuelve tx_id o None si falta saldo.
        """
        if fee_sync is None:
            fee_atto = MIN_FEE_ATTO
        else:
            fee_atto = self.sync_to_atto(fee_sync)
            if fee_atto < MIN_FEE_ATTO:
                fee_atto = MIN_FEE_ATTO

        timestamp = time.time()

        if batch:
            items = []
            total_amount_atto = 0
            for item in batch:
                to_n = item.get("to_node")
                amt_atto = self.sync_to_atto(item.get("amount_sync", 0))
                items.append({
                    "to_node": to_n,
                    "amount_atto": amt_atto,
                    "data_type": item.get("data_type", "generic"),
                    "data": item.get("data")
                })
                total_amount_atto += amt_atto

            if total_amount_atto + fee_atto > self.balances.get(from_node, 0):
                print(f"[ERROR] {from_node} saldo insuficiente para batch (necesita {self.atto_to_sync_str(total_amount_atto + fee_atto)} SYNC).")
                return None

            tx = {
                "tx_id": hashlib.sha256(f"{timestamp}-{from_node}-batch".encode()).hexdigest()[:16],
                "timestamp": timestamp,
                "from_node": from_node,
                "batch": items,
                "fee_atto": fee_atto
            }
            self.pending_transactions.append(tx)
            return tx["tx_id"]

        else:
            amount_atto = self.sync_to_atto(amount_sync)
            if amount_atto + fee_atto > self.balances.get(from_node, 0):
                print(f"[ERROR] {from_node} saldo insuficiente (necesita {self.atto_to_sync_str(amount_atto + fee_atto)} SYNC).")
                return None

            tx = {
                "tx_id": hashlib.sha256(f"{timestamp}-{from_node}-{to_node}".encode()).hexdigest()[:16],
                "timestamp": timestamp,
                "from_node": from_node,
                "to_node": to_node,
                "amount_atto": amount_atto,
                "data_type": data_type,
                "data": data,
                "fee_atto": fee_atto
            }
            self.pending_transactions.append(tx)
            return tx["tx_id"]

    # ---------- minado ----------
    def mine_block(self, ia_proof, miner_node, ai_data=None):
        """
        Crea bloque incluyendo mempool, aplica reward y fees, actualiza balances
        """
        # Si no hay tx pendientes y no quedan rewards, no hay nada que minar
        if not self.pending_transactions and self.current_block_reward(len(self.chain)) == 0:
            print("No pending txs y no quedan recompensas -> nada que minar.")
            return None

        reward_atto = self.current_block_reward(len(self.chain))
        total_fees_atto = sum(tx.get("fee_atto", 0) for tx in self.pending_transactions)

        # Copiamos transacciones
        block_txs = list(self.pending_transactions)

        # Añadimos transacción de reward (SYSTEM -> miner)
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

        # Crear bloque usando argumentos por nombre (compatible con Block)
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_last_block().hash,
            ia_proof=ia_proof,
            transactions=block_txs,
            ai_data=ai_data or {},
            nonce=0
        )

        # PoW ligero (simulación) — ajustable o reemplazable por Proof-of-IA
        # Aquí usamos sólo 1 leading zero para mantener rapidez en pruebas
        while not new_block.hash.startswith("0" * 1):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()

        # Añadir y aplicar efectos
        self.chain.append(new_block)
        self._apply_transactions_and_fees(new_block.transactions, miner_node)

        # Limpiar mempool
        self.pending_transactions = []

        print(f"Bloque {new_block.index} minado. reward={self.atto_to_sync_str(reward_atto)} SYNC, fees={self.atto_to_sync_str(total_fees_atto)} SYNC")
        return new_block

    # Aplica movimientos y paga fees al minero
    def _apply_transactions_and_fees(self, transactions, miner_node):
        total_fees = 0
        for tx in transactions:
            fee = tx.get("fee_atto", 0)
            total_fees += fee

            if "batch" in tx:
                sender = tx["from_node"]
                total_batch = sum(item["amount_atto"] for item in tx["batch"])
                if sender != "SYSTEM":
                    self.balances[sender] = self.balances.get(sender, 0) - total_batch - fee
                for item in tx["batch"]:
                    to = item["to_node"]
                    amt = item["amount_atto"]
                    self.balances[to] = self.balances.get(to, 0) + amt
            else:
                sender = tx.get("from_node")
                to = tx.get("to_node")
                amt = tx.get("amount_atto", 0)
                if amt > 0:
                    if sender != "SYSTEM":
                        self.balances[sender] = self.balances.get(sender, 0) - amt - fee
                    self.balances[to] = self.balances.get(to, 0) + amt
                else:
                    # data-only tx -> solo cobrar fee al remitente
                    if sender != "SYSTEM":
                        self.balances[sender] = self.balances.get(sender, 0) - fee

        # acreditar las fees totales al minero
        if total_fees > 0:
            self.balances[miner_node] = self.balances.get(miner_node, 0) + total_fees

    # ---------- consultas ----------
    def get_balance(self, node_id):
        return self.balances.get(node_id, 0)

    def get_balance_sync_str(self, node_id):
        return self.atto_to_sync_str(self.get_balance(node_id))

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i - 1]
            if cur.hash != cur.calculate_hash():
                print(f"Invalid hash at block {cur.index}")
                return False
            if cur.previous_hash != prev.hash:
                print(f"Invalid previous_hash at block {cur.index}")
                return False
        return True

    def get_all_transactions(self):
        all_txs = []
        for block in self.chain:
            all_txs.extend(block.transactions)
        return all_txs
