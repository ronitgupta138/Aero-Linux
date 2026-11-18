import unittest
from aero.btrfs_retention import evaluate_snapshot_pruning

class TestBtrfsRetention(unittest.TestCase):
    def test_pruning_count(self):
        self.assertEqual(evaluate_snapshot_pruning(15, 10), 5)
        self.assertEqual(evaluate_snapshot_pruning(5, 10), 0)
        self.assertEqual(evaluate_snapshot_pruning(10, 10), 0)

    def test_negative_count_throws(self):
        with self.assertRaises(ValueError):
            evaluate_snapshot_pruning(-1, 10)
