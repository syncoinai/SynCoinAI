import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from decimal import Decimal
from src.blockchain.chain import Blockchain

class TestSynCoinAIFull(unittest.TestCase):

    def setUp(self):
        self.bc = Blockchain()
        self.miner = "miner1"
        self.receiver1 = "alice"
        self.receiver2 = "bob"

    def test_genesis_block(self):
        genesis = self.bc.chain[0]
        self.assertEqual(genesis.index, 0)
        self.assertEqual(genesis.previous_hash, "0")
        self.assertTrue(len(genesis.hash) > 0)

    def test_mining_reward_and_supply(self):
        initial_reward_atto = self.bc.mining_reward_atto
        reward = self.bc.current_block_reward(len(self.bc.chain))
        self.assertEqual(reward, initial_reward_atto)

        for i in range(self.bc.blocks_per_halving):
            self.bc.mine_block(f"proof{i}", miner_node=self.miner)

        reward_post_halving = self.bc.current_block_reward(len(self.bc.chain))
        expected = initial_reward_atto // 2
        self.assertEqual(reward_post_halving, expected)

        # Simular near total supply
        self.bc.total_minted = self.bc.TOTAL_SUPPLY_ATTO - self.bc.sync_to_atto(5)
        reward = self.bc.current_block_reward(len(self.bc.chain))
        self.assertLessEqual(reward, self.bc.sync_to_atto(5))

    def test_simple_transaction(self):
        self.bc.mine_block("proof1", self.miner)
        tx_id = self.bc.add_transaction(self.miner, self.receiver1, amount_sync=5)
        self.assertIsNotNone(tx_id)
        self.bc.mine_block("proof2", self.miner)
        balance = Decimal(self.bc.get_balance(self.receiver1)) / Decimal(10**18)
        self.assertEqual(balance, Decimal("5"))

    def test_batch_transaction(self):
        self.bc.mine_block("proof1", self.miner)
        batch = [
            {"to_node": self.receiver1, "amount_sync": 1.2},
            {"to_node": self.receiver2, "amount_sync": 0.8},
        ]
        tx_id = self.bc.add_transaction(self.miner, batch=batch)
        self.assertIsNotNone(tx_id)
        self.bc.mine_block("proof2", self.miner)
        b1 = Decimal(self.bc.get_balance(self.receiver1)) / Decimal(10**18)
        b2 = Decimal(self.bc.get_balance(self.receiver2)) / Decimal(10**18)
        self.assertEqual(b1, Decimal("1.2"))
        self.assertEqual(b2, Decimal("0.8"))

    def test_minimum_fee_applied(self):
        self.bc.mine_block("proof1", self.miner)
        tx_id = self.bc.add_transaction(self.miner, self.receiver1, amount_sync=1, fee_sync=0)
        self.assertIsNotNone(tx_id)
        self.bc.mine_block("proof2", self.miner)
        miner_balance = self.bc.get_balance(self.miner)
        self.assertGreater(miner_balance, 0)

    def test_chain_validation(self):
        self.bc.mine_block("proof1", self.miner)
        self.bc.add_transaction(self.miner, self.receiver1, amount_sync=2)
        self.bc.mine_block("proof2", self.miner)
        self.assertTrue(self.bc.is_chain_valid())
        self.bc.chain[1].transactions[0]["amount_atto"] += 1
        self.assertFalse(self.bc.is_chain_valid())

    def test_balances_with_decimals(self):
        self.bc.mine_block("proof1", self.miner)
        tx_id = self.bc.add_transaction(self.miner, self.receiver1, amount_sync=0.000000000000000001)
        self.bc.mine_block("proof2", self.miner)
        balance = Decimal(self.bc.get_balance(self.receiver1)) / Decimal(10**18)
        self.assertEqual(balance, Decimal("0.000000000000000001"))

    def test_total_supply_not_exceeded(self):
        self.bc.total_minted = self.bc.TOTAL_SUPPLY_ATTO - 1
        reward = self.bc.current_block_reward(len(self.bc.chain))
        self.assertLessEqual(reward, 1)

if __name__ == "__main__":
    unittest.main()

