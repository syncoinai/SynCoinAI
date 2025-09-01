import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.blockchain.chain import Blockchain
from decimal import Decimal

def print_menu():
    print("\n=== SYNC ADVANCED INTERACTIVE TEST ===")
    print("1. Minar bloque")
    print("2. Enviar transacción simple")
    print("3. Enviar transacción batch")
    print("4. Mostrar balance de nodo")
    print("5. Mostrar blockchain resumido")
    print("6. Validar blockchain")
    print("7. Historial de transacciones de nodo")
    print("8. Reporte de supply y recompensas")
    print("0. Salir")

def main():
    bc = Blockchain()
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
                print(f"Bloque minado #{block.index} con hash {block.hash[:12]}..., recompensa: {reward_sync} SYNC")
        
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
            print(f"Balance {node}: {balance} SYNC")

        elif choice == "5":
            print("\n=== Blockchain Resumido ===")
            for block in bc.chain:
                print(f"Block {block.index}: {len(block.transactions)} txs, hash {block.hash[:12]}..., reward {Decimal(block.reward_atto)/Decimal(10**18)} SYNC")

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
            print(f"Recompensa actual por bloque: {Decimal(bc.current_block_reward(len(bc.chain)))/Decimal(10**18)} SYNC")
            print("Balances actuales de todos los nodos:")
            for node, bal_atto in bc.balances.items():
                bal_sync = Decimal(bal_atto)/Decimal(10**18)
                print(f"  {node}: {bal_sync} SYNC")

        elif choice == "0":
            print("Saliendo del interactive test avanzado...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
