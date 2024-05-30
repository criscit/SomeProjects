from typing import List, Optional


class Node:
    x: int
    _next: "Node"

    def __init__(self, x: int, _next: Optional["Node"] = None):
        self.x = x
        self._next = _next


class LinkedList:
    def __init__(self):
        # Pointer to the beginning of the list
        self.begin: Optional[Node] = None

    def push_front(self, x: int) -> None:
        """Adds element to the beginning of the list."""
        # TODO IMPLEMENT THIS

    def print(self) -> None:
        """This function could be useful for debugging and testing."""
        n = self.begin
        while n is not None:
            print(n.x, end=" ")
            n = n._next
        print()

    def copy_every_second(self) -> "LinkedList":
        """
        This function should return copy of the list where every second element
        is removed. Initial list should not be changed. E.g. if we run
        copy_every_second on list [1, 2, 3, 4, 5, 6, 7, 100, 120, 162, 0, 1] new
        list with values [1, 3, 5, 7, 120, 0] should be returned.
        """
        # TODO IMPLEMENT THIS
        return LinkedList()

    def get_size(self) -> int:
        """Returns number of elements in list."""
        #  TODO IMPLEMENT THIS
        return 0

    def to_array(self) -> List[Optional[int]]:
        """
        Converts our list to an array. New array is created with values the
        same as in list.
        """
        # TODO IMPLEMENT THIS
        return [None]*0

    def remove_after(self, x: Node) -> None:
        """
        Removes elements x._next from the list.
        O(1) time is expected.
        """
        # TODO IMPLEMENT THIS

    def insert_after(self, x: Node, val: int):
        """
        Inserts new element with value val right after the element x.
        O(1) time is expected
        """
        # TODO IMPLEMENT THIS

    def filter_divisible(self, x: int):
        """
        Removes all elements from the list that are divisible by x.
        E.g. list {1, 2, 3, 4, 4, 10, 7}  after filter_divisible(2) would look like {1, 3, 7}.
        O(N) time is expected.
        """
        # TODO IMPLEMENT THIS

    def get_at(self, index: int) -> Optional[Node]:
        """Returns Node from the list by index. O(N) time is expected."""
        # TODO IMPLEMENT THIS
        return None

    @classmethod
    def from_array(cls, a: List[int]) -> "LinkedList":
        """Creates LinkedList from python list."""
        l = cls()
        for item in a:
            l.push_front(item)
        return l
