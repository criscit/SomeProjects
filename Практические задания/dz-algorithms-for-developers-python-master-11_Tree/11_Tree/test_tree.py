from typing import Set, List
from unittest import TestCase
import random

import tree


class TestNode(tree.Node):
    def __init__(self, current_depth: int):
        super().__init__()
        self.current_depth = current_depth
        self.id = None
        self.parent: "TestNode" = None


class TreeTest(TestCase):
    def test_depth(self):
        """Tree depth."""
        self.assertEqual(0, tree.max_depth(None))
        self.assertEqual(1, tree.max_depth(TestNode(0)))

        node = self.tree_creator(10, 5, set())
        self.assertEqual(self.max_depth(node), tree.max_depth(node))

        node = self.tree_creator(10, 10, set())
        self.assertEqual(self.max_depth(node), tree.max_depth(node))

        node = self.tree_creator(10, 8, set())
        self.assertEqual(self.max_depth(node), tree.max_depth(node))

    def test_tree_build(self):
        """Tree build."""
        cases = [5, 6, 7, 8, 9]
        for min_depth in cases:
            with self.subTest(min_depth=min_depth):
                nodes: Set[TestNode] = set()
                test_node = self.tree_creator(10, min_depth, nodes)
                depth = self.max_depth(test_node)

                for i, node in enumerate(nodes):
                    node.id = i

                links: List[int] = []
                for node in nodes:
                    if node.parent is None:
                        links.append(-1)
                    else:
                        links.append(node.parent.id)
                arr = [node.virus for node in nodes]
                self.assertEqual(depth, self.max_depth(tree.from_list(links, arr)))

    def test_current_depth(self):
        """Tree depth."""
        cases = [5, 6, 7, 8, 9]
        for min_depth in cases:
            with self.subTest(min_depth=min_depth):
                nodes: Set[TestNode] = set()
                test_node = self.tree_creator(10, min_depth, nodes)
                curr_depth = {node for node in nodes if node.current_depth == min_depth - 1}
                user_lst = tree.all_on_curr_depth(test_node, min_depth - 1)

                self.assertIsNotNone(user_lst)
                self.assertEqual(curr_depth, user_lst)

    def test_lca(self):
        """LCA."""
        cases = [5, 6, 7, 8, 9]
        for min_depth in cases:
            with self.subTest(min_depth=min_depth):
                nodes: Set[TestNode] = set()
                test_node = self.tree_creator(10, min_depth, nodes)
                nodes_list: List[TestNode] = list(nodes)
                first = nodes_list[0]
                second = nodes_list[-1]

                firstParents: Set[TestNode] = set()
                node = first
                while True:
                    firstParents.add(node)
                    if not node.parent:
                        break
                    node = node.parent

                secondParents: Set[TestNode] = set()
                node = second
                while True:
                    secondParents.add(node)
                    if not node.parent:
                        break
                    node = node.parent

                firstParents &= secondParents
                ans = min(firstParents, key=lambda i: i.current_depth) or test_node

                self.assertEqual(ans, tree.lca(first, second));

    def tree_creator(self, max_child: int, max_depth: int, nodes: Set[TestNode]):
        test_node = TestNode(0)
        nodes.add(test_node)
        self.tree_gen(test_node, max_child, max_depth, 1, nodes)
        return test_node

    def max_depth(self, node: tree.Node) -> int:
        if not node:
            return 0

        depths: List[int] = []
        for n in node.v:
            depths.append(self.max_depth(n))
        if not depths:
            return 1
        return max(depths) + 1

    def tree_gen(self, root: TestNode, max_child: int, max_depth: int, current_depth: int, nodes: Set[TestNode]):
        if current_depth == max_depth:
            return
        child = random.randrange(0, max_child)
        test_node = TestNode(current_depth)
        root.v.append(test_node)
        test_node.parent = root
        nodes.add(test_node)
        current_depth += 1
        for i in range(child):
            self.tree_gen(test_node, max_child, max_depth, current_depth, nodes)
