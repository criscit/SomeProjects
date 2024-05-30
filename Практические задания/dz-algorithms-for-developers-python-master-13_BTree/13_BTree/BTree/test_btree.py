from unittest import TestCase
import random

from btree import BTree

N = 1_000_000


class BTreeTest(TestCase):
    def test_btree(self):
        tree = BTree()
        a = [i*2 for i in range(N)]
        random.shuffle(a)
        for i in a:
            tree.add(i)

        for item in [-10, 1, 12_381, 99_115]:
            self.assertNotIn(item, tree, f"Node <{item}> unexpectedly found in Btree!")

        for item in [0, 4, 1_230, 87_612, 1_230_000]:
            self.assertIn(item, tree, f"Node <{item}> unexpectedly NOT found in Btree!")

        for i, item in enumerate(tree.get_sorted()):
            self.assertEqual(i*2, item)

        self.assertLess(tree.get_max_height(), 1000)
