from unittest import TestCase

from list_node import ListNode
from merge_sort_recursion import merge_two_lists, merge_three_lists


class MergeSortRecursionTest:
    def is_sorted(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        return (head.val <= head.next.val and self.is_sorted(head.next))

    def get_list_length(self, node: ListNode) -> int:
        if node is None:
            return 0
        return 1 + self.get_list_length(node.next)

    def test_merge_2_linked_lists(self):
        """Merge 2 sorted LinkedList"""
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        cases = [
            (l1, l2, 6),
            (None, ListNode(5), 1),
            (None, None, 0),
        ]
        for i, l1, l2, size in enumerate(cases):
            with self.subTest(f"case = {i}"):
                actual = merge_two_lists(l1, l2)
                self.assertTrue(self.is_sorted(actual))
                self.assertEqual(self.get_list_length(actual), size)

    def test_merge_2_linked_lists(self):
        """Merge 3 sorted LinkedList."""
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)
        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)
        l3 = ListNode(2)
        l3.next = ListNode(4)
        l3.next.next = ListNode(6)

        cases = [
            (l1, l2, l3, 9),
            (None, ListNode(5), None, 1),
            (ListNode(1), ListNode(5), None, 2),
            (None, None, None, 0)
        ]
        for i, l1, l2, l3, size in enumerate(cases):
            with self.subTest(f"case = {i}"):
                actual = merge_three_lists(l1, l2, l3)
                self.assertTrue(self.is_sorted(actual))
                self.assertEqual(self.get_list_length(actual), size)
