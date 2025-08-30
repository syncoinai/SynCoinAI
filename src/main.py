from blockchain.chain import Blockchain
import hashlib

def simulate_ia_proof(ai_data):
    """
    Simula la generación de un hash único por la IA
    ai_data: string o dict representando datos de IA
    """
    data_string = str(ai_data)
    return hashlib.sha256(data_string.encode()).hexdigest()

def main():
    # Crear blockchain
    my_chain = Blockchain()

    # Añadir transacciones entre nodos de IA
    my_chain.add_transaction("AI_Node_1", "AI_Node_2", "Model weights v1", data_type="model_weights")
    my_chain.add_transaction("AI_Node_2", "AI_Node_3", "Inference results", data_type="inference_result")

    # Generar prueba de IA para primer bloque
    ia_proof = simulate_ia_proof("First block AI data")

    # Minar primer bloque con transacciones y prueba de IA
    my_chain.mine_block(ia_proof, ai_data={"model": "v1", "accuracy": 0.87})

    # Añadir más transacciones
    my_chain.add_transaction("AI_Node_3", "AI_Node_1", "Updated model v2", data_type="model_weights")

    # Generar prueba de IA para segundo bloque
    ia_proof2 = simulate_ia_proof("Second block AI data")

    # Minar segundo bloque
    my_chain.mine_block(ia_proof2, ai_data={"model": "v2", "accuracy": 0.92})

    # Mostrar blockchain completa
    print("=== SynCoinAI Blockchain ===")
    print(my_chain)

    # Validar blockchain
    print("\nBlockchain valid?", my_chain.is_valid())

    # Mostrar todas las transacciones
    print("\nAll transactions in blockchain:")
    for tx in my_chain.get_all_transactions():
        print(tx)

if __name__ == "__main__":
    main()
