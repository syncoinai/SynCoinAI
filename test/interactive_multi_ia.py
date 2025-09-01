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

ia_nodes = [f"IA_Node_{i+1}" for i in range(NUM_IA)]
bc = Blockchain()
lock = threading.Lock()
rewards_record = {node: Decimal(0) for node in ia_nodes}

def print_menu():
    print("\n=== SYNC INTERACTIVE + MULTI-IA ===")
    print("1. Minar bloque")
    print("2. Enviar transacción simple")
    print("3. Enviar transacción batch")
    print("4. Mostrar balance de nodo")
    print("5. Mostrar blockchain resumido")
    print("6. Validar blockchain")
    print("7. Historial de transacciones de nodo")
    print("8. Reporte de supply y recompensas")
    print("9. Simular múltiples IA")
    print("0. Salir")

def ia_worker(node_id):
    for block_num in range(NUM_BLOCKS):
        for _ in range(TX_PER_IA):
            receiver = random.choice([n for n in ia_nodes if n != node_id])
            amount = round(random.uniform(0.01, 0.1), 18)
            fee = random.uniform(1e-12, 1e-9)
            with lock:
                bc.add_transaction(node_id, receiver, amount_sync=amount, fee_sync=fee)
            time.sleep(SLEEP_BETWEEN_ACTIONS)
        proof = f"{node_id}_proof_{block_num}"
        with lock:
            block = bc.mine_block(ia_proof=proof, miner_node=node_id)
        reward_sync = Decimal(block.reward_atto) / Decimal(10**18)
        rewards_record[node_id] += reward_sync
        print(f"{node_id} minó bloque #{block.index}, reward {reward_sync:.12f} SYNC")

def simulate_multi_ia():
    threads = []
    for node in ia_nodes:
        t = threading.Thread(target=ia_worker, args=(node,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("\n=== SIMULACIÓN MULTI-IA COMPLETADA ===")
    print("Balances finales de nodos:")
    for node in ia_nodes:
        bal = Decimal(bc.get_balance(node))/Decimal(10**18)
        print(f"  {node}: {bal:.12f} SYNC (recompensas: {rewards_record[node]:.12f})")
    print(f"Blockchain válida: {bc.is_chain_valid()}")

def main():
    print("Blockchain SYNC inicializada (total supply: 21M SYNC, 18 decimales).")
    while True:
        print_menu()
        choice = input("Opción: ").strip()

        if choice == "1":
            miner = input("Miner node ID: ").strip()
            proof = input("IA proof (string): ").strip()
            block = bc.mine_block(ia_proof=proof, miner_node=miner)
            if block:
                reward_sync = Decimal(block.reward_atto) / Decimal(10**18)
                print(f"Bloque minado #{block.index}, recompensa: {reward_sync:.12f} SYNC")

        elif choice == "2":
            sender = input("From node: ").strip()
            receiver = input("To node: ").strip()
            amount = input("Amount (SYNC): ").strip()
            try:
                amount = float(amount)
            except ValueError:
                print("Cantidad inválida")
                continue
            tx_id = bc.add_transaction(sender, receiver, amount_sync=amount)
            print(f"Tx enviada con ID {tx_id}" if tx_id else "Error: saldo insuficiente o inválido.")

        elif choice == "3":
            sender = input("From node: ").strip()
            batch = []
            print("Introduce items para batch (vacío para terminar):")
            while True:
                to = input("  To node: ").strip()
                if not to:
                    break
                amt = input("  Amount (SYNC): ").strip()
                try:
                    amt = float(amt)
                except ValueError:
                    print("Cantidad inválida")
                    continue
                batch.append({"to_node": to, "amount_sync": amt})
            tx_id = bc.add_transaction(sender, batch=batch)
            print(f"Batch enviado con ID {tx_id}" if tx_id else "Error: saldo insuficiente o inválido.")

        elif choice == "4":
            node = input("Node ID: ").strip()
            balance = Decimal(bc.get_balance(node)) / Decimal(10**18)
            print(f"Balance {node}: {balance:.12f} SYNC")

        elif choice == "5":
            print("\n=== Blockchain Resumido ===")
            for block in bc.chain:
                print(f"Block {block.index}: {len(block.transactions)} txs, hash {block.hash[:12]}..., reward {Decimal(block.reward_atto)/Decimal(10**18):.12f} SYNC")

        elif choice == "6":
            print("Blockchain válida" if bc.is_chain_valid() else "Blockchain corrupta!")

        elif choice == "7":
            node = input("Node ID: ").strip()
            txs = bc.get_node_transactions(node)
            print(f"Transacciones de {node}:")
            for tx in txs:
                print(f"  TxID: {tx['tx_id']}, Amount: {Decimal(tx.get('amount_atto',0))/Decimal(10**18)} SYNC, Type: {tx.get('data_type')}")

        elif choice == "8":
            total_minted = Decimal(bc.total_minted)/Decimal(10**18)
            print(f"Total SYNC emitidos: {total_minted} SYNC")
            print(f"Recompensa actual por bloque: {Decimal(bc.current_block_reward(len(bc.chain)))/Decimal(10**18):.12f} SYNC")
            print("Balances actuales de todos los nodos:")
            for node, bal_atto in bc.balances.items():
                bal_sync = Decimal(bal_atto)/Decimal(10**18)
                print(f"  {node}: {bal_sync:.12f} SYNC")

        elif choice == "9":
            simulate_multi_ia()

        elif choice == "0":
            print("Saliendo del modo interactivo + multi-IA...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
    