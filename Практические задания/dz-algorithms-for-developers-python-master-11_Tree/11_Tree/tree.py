from typing import List


MISSING = object()


class Virus:
    pass


class Node:
    def __init__(self, virus: Virus = MISSING):
        self.virus = virus
        if self.virus is MISSING:
            self.virus = Virus()

        self.v = []


def max_depth(root: Node) -> int:
    return 0


def from_list(index: List[int], elements: List[Virus]) -> Node:
    return None


def all_on_curr_depth(root: Node, generation: int) -> List[Node]:
    return None


def lca(first: Node, second: Node) -> Node:
    return None
