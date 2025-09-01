import sys
import os
import threading
import time
import random
from decimal import Decimal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.blockchain.chain import Blockchain

# Parámetros de simulación
NUM_IA = 5
NUM_BLOCKS = 10
TX_PER_IA = 3
SLEEP_BETWEEN_ACTIONS = 0.05  # segundos

# Inicializar nodos IA y blockchain
ia_nodes = [f"IA_Node_{i+1}" for i in range(NUM_IA)]
bc = Blockchain()
lock = threading.Lock()

# Historial de recompensas
rewards_record = {node: Decimal(0) for node in ia_nodes}

def ia_worker(node_id):
    for block_num in range(NUM_BLOCKS):
        # 1️⃣ Enviar transacciones pendientes
        for _ in range(TX_PER_IA):
            receiver = random.choice([n for n in ia_nodes if n != node_id])
            amount = round(random.uniform(0.01, 0.1), 18)  # Cantidad pseudoaleatoria con 18 decimales
            fee = random.uniform(1e-12, 1e-9)
            with lock:
                bc.add_transaction(node_id, receiver, amount_sync=amount, fee_sync=fee)
            time.sleep(SLEEP_BETWEEN_ACTIONS)

        # 2️⃣ Minar bloque con pool de transacciones
        proof = f"{node_id}_proof_{block_num}"
        with lock:
            block = bc.mine_block(ia_proof=proof, miner_node=node_id)
        reward_sync = Decimal(block.reward_atto) / Decimal(10**18)
        rewards_record[node_id] += reward_sync
        print(f"{node_id} minó bloque #{block.index} con {len(block.transactions)} txs y recompensa {reward_sync:.12f} SYNC")

threads = []

# Lanzar threads
for node in ia_nodes:
    t = threading.Thread(target=ia_worker, args=(node,))
    t.start()
    threads.append(t)

# Esperar a que todas las IA terminen
for t in threads:
    t.join()

# Resultados finales
print("\n=== SIMULACIÓN AVANZADA COMPLETADA ===")
print("Blockchain resumida:")
for block in bc.chain:
    print(f"Block {block.index}: {len(block.transactions)} txs, hash {block.hash[:12]}..., reward {Decimal(block.reward_atto)/Decimal(10**18):.12f} SYNC")

print("\nBalances finales de nodos:")
for node in ia_nodes:
    bal = Decimal(bc.get_balance(node)) / Decimal(10**18)
    print(f"  {node}: {bal:.12f} SYNC (recompensas acumuladas: {rewards_record[node]:.12f} SYNC)")

print(f"\nBlockchain válida: {bc.is_chain_valid()}")
