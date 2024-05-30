from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next
