import sys
import shlex
from blockchain.chain import Blockchain
from decimal import Decimal

# Inicializar blockchain
blockchain = Blockchain()
blockchain.balances["alice"] = Blockchain.sync_to_atto(1000)
blockchain.balances["bob"] = Blockchain.sync_to_atto(500)
blockchain.balances["miner1"] = 0

HELP_TEXT = """
Comandos disponibles:
  help                     -> Mostrar este mensaje
  show_chain               -> Mostrar blockchain resumida
  tx <from> <to> <amt> [data] -> Crear transacción simple
  batch_tx <from>          -> Crear transacción batch (se piden sub-transfers)
  mempool                  -> Mostrar transacciones pendientes
  mine <miner_node> <ia_proof> -> Minar un bloque
  balances                 -> Mostrar balances de todos los nodos
  all_txs                  -> Mostrar todas las transacciones
  validate                 -> Validar blockchain
  exit                     -> Salir
"""

def cmd_show_chain(args):
    print("\n=== Blockchain Resumida ===")
    for block in blockchain.chain:
        print(f"Block {block.index} | hash={block.hash[:16]}... | prev={block.previous_hash[:16]}...")
        print(f"  txs: {len(block.transactions)}, ai_data: {block.ai_data}")
    print("===========================")

def cmd_tx(args):
    if len(args) < 3:
        print("Uso: tx <from> <to> <amt> [data]")
        return
    from_node, to_node, amt = args[:3]
    data = args[3] if len(args) > 3 else None
    try:
        tx_id = blockchain.add_transaction(from_node, to_node, amount_sync=amt, data=data)
        if tx_id:
            print(f"Transacción creada: {tx_id}")
    except Exception as e:
        print(f"Error: {e}")

def cmd_batch_tx(args):
    if len(args) < 1:
        print("Uso: batch_tx <from>")
        return
    from_node = args[0]
    batch = []
    print("Introduce sub-transfers (vacío para terminar):")
    while True:
        to = input("  -> A (node_id): ").strip()
        if not to:
            break
        amt = input("  -> Monto en SYNC: ").strip()
        batch.append({"to_node": to, "amount_sync": amt})
    if batch:
        tx_id = blockchain.add_transaction(from_node, batch=batch)
        if tx_id:
            print(f"Batch tx creada: {tx_id}")

def cmd_mine(args):
    if len(args) < 2:
        print("Uso: mine <miner_node> <ia_proof>")
        return
    miner_node, ia_proof = args[:2]
    block = blockchain.mine_block(miner_node=miner_node, ia_proof=ia_proof, ai_data={"note": "mined via interactive_main"})
    if block:
        print(f"Bloque {block.index} minado por {miner_node}. Hash={block.hash[:16]}...")

def cmd_balances(args):
    print("\n=== Balances ===")
    for node, balance in blockchain.balances.items():
        print(f"{node}: {blockchain.atto_to_sync_str(balance)} SYNC")

def cmd_mempool(args):
    print("\n=== Mempool ===")
    for tx in blockchain.pending_transactions:
        print(tx)
    if not blockchain.pending_transactions:
        print("Mempool vacío.")

def cmd_all_txs(args):
    print("\n=== Todas las transacciones ===")
    for tx in blockchain.get_all_transactions():
        print(tx)

def cmd_validate(args):
    print("Validando blockchain...")
    if blockchain.is_chain_valid():
        print("✅ Blockchain válida")
    else:
        print("❌ Blockchain inválida")

COMMANDS = {
    "help": lambda args: print(HELP_TEXT),
    "show_chain": cmd_show_chain,
    "tx": cmd_tx,
    "batch_tx": cmd_batch_tx,
    "mine": cmd_mine,
    "balances": cmd_balances,
    "mempool": cmd_mempool,
    "all_txs": cmd_all_txs,
    "validate": cmd_validate,
    "exit": lambda args: sys.exit(0)
}

def main():
    print("=== SynCoinAI CLI ===")
    print("Escribe 'help' para ver comandos disponibles.")
    while True:
        try:
            raw_input = input("SYNC> ").strip()
            if not raw_input:
                continue
            parts = shlex.split(raw_input)
            cmd = parts[0]
            args = parts[1:]
            if cmd in COMMANDS:
                COMMANDS[cmd](args)
            else:
                print(f"Comando desconocido: {cmd}. Escribe 'help' para ayuda.")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
