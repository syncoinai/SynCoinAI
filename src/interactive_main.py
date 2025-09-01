from blockchain.chain import Blockchain

def print_menu():
    print("\n=== MENU ===")
    print("1. Minar bloque")
    print("2. Enviar transacción simple")
    print("3. Enviar transacción batch")
    print("4. Ver balance")
    print("5. Mostrar blockchain")
    print("6. Validar blockchain")
    print("0. Salir")

def main():
    bc = Blockchain()
    print("Blockchain SYNC inicializada con supply máximo de 21M SYNC (18 decimales).")

    while True:
        print_menu()
        choice = input("Opción: ").strip()

        if choice == "1":
            miner = input("Miner node ID: ")
            proof = input("IA proof (string): ")
            block = bc.mine_block(ia_proof=proof, miner_node=miner)
            if block:
                print(f"Bloque minado #{block.index}, hash={block.hash[:12]}...")

        elif choice == "2":
            sender = input("From node: ")
            receiver = input("To node: ")
            amount = input("Amount (SYNC): ")
            try:
                amount = float(amount)
            except:
                print("Cantidad inválida.")
                continue
            tx_id = bc.add_transaction(sender, receiver, amount_sync=amount)
            if tx_id:
                print(f"Tx enviada con ID {tx_id}")

        elif choice == "3":
            sender = input("From node: ")
            batch = []
            print("Introduce items (vacío para terminar):")
            while True:
                to = input("  To node: ").strip()
                if not to:
                    break
                amt = float(input("  Amount (SYNC): "))
                batch.append({"to_node": to, "amount_sync": amt})
            if not batch:
                print("Batch vacío, cancelado.")
                continue
            tx_id = bc.add_transaction(sender, batch=batch)
            if tx_id:
                print(f"Batch enviado con ID {tx_id}")

        elif choice == "4":
            node = input("Node ID: ")
            print(f"Balance {node}: {bc.get_balance_sync_str(node)} SYNC")

        elif choice == "5":
            for block in bc.chain:
                print(block.to_dict())

        elif choice == "6":
            print("Blockchain válida" if bc.is_chain_valid() else "Blockchain corrupta!")

        elif choice == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
