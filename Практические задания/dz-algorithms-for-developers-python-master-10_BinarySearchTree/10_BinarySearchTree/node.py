from typing import Optional, Any


class Node:
    def __init__(self, x: Any, parent: "Node"):
        self.x = x
        self.parent = parent
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def __str__(self) -> str:
        return f"Node x={self.x}"
