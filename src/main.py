from blockchain.chain import Blockchain

def main():
    # Crear blockchain
    bc = Blockchain()

    # Minar primer bloque (genera recompensa)
    bc.mine_block(ia_proof="demo_proof", miner_node="miner1")

    # Crear algunas transacciones
    bc.add_transaction("miner1", "alice", amount_sync=5, data_type="payment", data="primer pago")
    bc.add_transaction("miner1", "bob", amount_sync=2.5, data_type="payment", data="segundo pago")
    bc.add_transaction("miner1", data_type="note", data="transacción solo con datos")

    # Batch transaction
    bc.add_transaction(
        "miner1",
        batch=[
            {"to_node": "carol", "amount_sync": 1.0, "data_type": "payment"},
            {"to_node": "dave", "amount_sync": 0.5, "data_type": "payment"},
        ]
    )

    # Minar segundo bloque
    bc.mine_block(ia_proof="demo_proof2", miner_node="miner1", ai_data={"summary": "bloque con txs"})

    # Mostrar balances
    for user in ["miner1", "alice", "bob", "carol", "dave"]:
        print(f"Balance {user}: {bc.get_balance_sync_str(user)} SYNC")

    # Mostrar estado de la cadena
    print("\n=== Blockchain ===")
    for block in bc.chain:
        print(block)

if __name__ == "__main__":
    main()
