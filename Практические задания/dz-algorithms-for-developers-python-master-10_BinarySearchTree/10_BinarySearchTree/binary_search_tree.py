from typing import List

from node import Node
from receipt import Receipt


def from_list(elements: List[Receipt]) -> Node:
    pass


def from_node(root: Node) -> List[Receipt]:
    pass


def get_amount(root: Node, receipt_number: int) -> float:
    pass


def check_tree(root: Node) -> bool:
    pass


def delete(root: Node, receipt: Receipt) -> Node:
    """Returns new root (in case old root was deleted)."""
    pass


def get_next(root: Node, receipt: Receipt) -> Receipt:
    pass
