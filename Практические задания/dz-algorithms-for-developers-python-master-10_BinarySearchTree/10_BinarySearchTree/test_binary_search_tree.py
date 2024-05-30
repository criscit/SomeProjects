from unittest import TestCase
import random

import binary_search_tree
from receipt import Receipt
from node import Node


class BinarySearchTreeTest(TestCase):
    def test_build_tree_from_list(self):
        """Building tree."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        random.shuffle(receipts)

        root = binary_search_tree.from_list(receipts)

        self.assertEqual(root.parent, None)
        self.assertEqual(root.x.amount, 8)

        self.assertEqual(root.left.left.left.x.receipt_number, 0)
        self.assertEqual(root.left.left.x.receipt_number, 1)
        self.assertEqual(root.left.x.receipt_number, 2)
        self.assertEqual(root.left.right.x.receipt_number, 3)
        self.assertEqual(root.x.receipt_number, 4)
        self.assertEqual(root.right.left.left.x.receipt_number, 5)
        self.assertEqual(root.right.left.x.receipt_number, 6)
        self.assertEqual(root.right.x.receipt_number, 7)
        self.assertEqual(root.right.right.x.receipt_number, 8)

        self.assertEqual(root.right.right.left, None)
        self.assertEqual(root.right.right.right, None)
        self.assertEqual(root.left.left.right, None)

    def test_build_list_from_node(self):
        """Building list from tree."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        test_root = self.from_list_test(receipts)

        self.assertCountEqual(receipts, binary_search_tree.from_node(test_root))

    def test_amount_finder(self):
        """Search for amount."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        test_root = self.from_list_test(receipts)
        rec = random.choice(receipts)

        amount = binary_search_tree.get_amount(test_root, rec.receipt_number)

        self.assertEqual(amount, rec.amount)

    def test_is_bst(self):
        """Check tree."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        test_root = self.from_list_test(receipts)
        self.assertTrue(binary_search_tree.check_tree(test_root))

        test_root.left.x.receipt_number = 10
        self.assertFalse(binary_search_tree.check_tree(test_root))

    def test_delete(self):
        """Delete element."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        test_root = self.from_list_test(receipts)
        rec = random.choice(receipts)

        new_root = binary_search_tree.delete(test_root, rec)

        self.assertEqual(len(receipts), len(self.to_list_test(new_root)) + 1)

    def test_next_element(self):
        """Next element."""
        receipts = [Receipt(i, i * 2) for i in range(9)]
        test_root = self.from_list_test(receipts)
        rand = random.randint(0, len(receipts) - 5)

        next_node = binary_search_tree.get_next(test_root, receipts[rand])

        self.assertEqual(next_node, receipts[rand+1])
        self.assertEqual(binary_search_tree.get_next(test_root, receipts[-1], None))

    def from_list_test(self, elements):
        elements = sorted(elements, key=lambda i: i.receipt_number)
        def helper(left, right) -> Node:
            if left + 1 > right: return None
            if left + 1 == right: return Node(elements[left], None)

            m = (left + right) // 2
            t = Node(elements[m], None)
            t.left = helper(left, m)
            t.right = helper(m+1, right)
            if t.left:
                t.left.parent = t
            if t.right:
                t.right.parent = t
            return t

        return helper(0, len(elements))

    def to_list_test(self, root):
        res = []
        res.append(root.x)
        if root.left:
            res.extend(to_list_test(root.left))
        if root.right:
            res.extend(to_list_test(root.right))
        return res
