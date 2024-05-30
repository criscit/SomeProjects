from collections import deque
from unittest import TestCase

from simple_graph import Node, Employee, clone_graph_vk, get_importance


def BFS(start: Node):
    seen = set()
    queue = deque()
    result = ""

    seen.add(start)
    queue.append(start)

    while queue:
        cur = queue.pop()
        result += cur.val
        for node in cur.neighbors:
            if node in seen:
                continue
            seen.add(node)
            queue.add(node)

    return result


class SimpleGraphTest(TestCase):
    def test_get_importance(self):
        """Get importance of employee."""
        emp1 = Employee(1, 5, [2, 3])
        emp2 = Employee(2, 3, [])
        emp3 = Employee(3, 3, [])
        emp4 = Employee(4, 15, [5])
        emp5 = Employee(5, 10, [6])
        emp6 = Employee(6, 5, [])
        cases = [
            ([emp1, emp2, emp3], 1, 11),
            ([emp4, emp5, emp6], 4, 30),
        ]

        for i, (employees, id, expected_importance) in enumerate(cases):
            with self.subTest(case=i):
                actual = get_importance(employees, id)
                self.assertEqual(actual, expected_importance)

    def test_clone_graph_vk(self):
        """Help Ivan copy VK Graph."""
        ak1 = Node("Ivan")
        ak2 = Node("Maria")
        ak3 = Node("Kate")
        ak4 = Node("Peter")
        ak5 = Node("Anna")
        ak6 = Node("Emma")

        ak1.neighbors = [ak2, ak3]
        ak2.neighbors = [ak1, ak4]
        ak3.neighbors = [ak1, ak4]
        ak4.neighbors = [ak2, ak3, ak5, ak6]
        ak5.neighbors = [ak4]
        ak6.neighbors = [ak4]

        cases = [ak1, ak2, ak3, ak4, ak5, ak6]
        for i, root in enumerate(cases):
            with self.subTest(case=i):
                actual = BFS(clone_graph_vk(root))
                expected = BFS(root)
                self.assertEqual(actual, expected)
