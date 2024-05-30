from typing import List, Optional


class Employee:
    """Определение сотрудника."""
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Node:
    """Определение Node."""

    def __init__(self, val: str = "", neighbors: Optional[List["Node"]] = None):
        self.val = val
        if neighbors is None:
            neighbors = []
        self.neighbors = neighbors


def get_importance(employees: List[Employee], id: int) -> int:
    """Task #1."""
    # TODO please implement
    return -1


def clone_graph_vk(node: Node) -> Node:
    """Task #2."""
    # TODO please implement
    return None
