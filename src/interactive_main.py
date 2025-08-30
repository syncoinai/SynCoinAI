from blockchain.chain import Blockchain
import hashlib
import time

def simulate_ia_proof(ai_data):
    data_string = str(ai_data)
    return hashlib.sha256(data_string.encode()).hexdigest()

def main():
    my_chain = Blockchain()
    print("=== SynCoinAI Interactive Blockchain ===")

    while True:
        print("\nOpciones:")
        print("1 - Añadir transacción")
        print("2 - Minar bloque")
        print("3 - Mostrar blockchain")
        print("4 - Mostrar todas las transacciones")
        print("5 - Validar blockchain")
        print("0 - Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            from_node = input("Nodo emisor: ")
            to_node = input("Nodo receptor: ")
            data_type = input("Tipo de datos (model_weights, inference_result, etc.): ")
            data = input("Datos: ")
            tx_id = my_chain.add_transaction(from_node, to_node, data, data_type)
            print(f"Transacción añadida con ID: {tx_id}")

        elif choice == "2":
            ai_info = input("Introduce info de IA para el bloque: ")
            ia_proof = simulate_ia_proof(ai_info)
            block = my_chain.mine_block(ia_proof, ai_data={"info": ai_info})
            print(f"Bloque minado! Index: {block.index}, Hash: {block.hash[:10]}...")

        elif choice == "3":
            print("=== Blockchain ===")
            print(my_chain)

        elif choice == "4":
            print("=== Todas las transacciones ===")
            for tx in my_chain.get_all_transactions():
                print(tx)

        elif choice == "5":
            print("Blockchain válida?", my_chain.is_valid())

        elif choice == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
