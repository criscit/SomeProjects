"""Stack implemented using dynamic array inside."""


class Stack:
    def __init__(self):
        # Array where we store the data
        self.a = [None] * 10
        # Number of elements that we actually store in the array. <= a.length
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def reallocate(self) -> None:
        """
        This function is called when it's not enough memory to fit new elements.
        It creates new long array and copies all the elements there.
        """
        #  IMPLEMENT THIS

    def push_back(self, x: int) -> None:
        """Adds element to the end of the stack."""
        #  IMPLEMENT THIS

    def pop_back(self) -> int:
        """Removes last element from the stack and returns its value."""
        #  IMPLEMENT THIS
        return 0

    def top(self) -> int:
        """Returns value of the last element in the stack."""
        #  IMPLEMENT THIS
        return 0


def calc_polish(s: str) -> int:
    """
    Calculates the result of reversed polish notation. https://en.wikipedia.org/wiki/Reverse_Polish_notation
    This one is simplified. Every number and character are separated by exactly one space.
    Only + - * should be supported.

    >>> calcPolish("1 2 3 * -")
    -5
    # because (1 - (2 * 3))
    """
    #  IMPLEMENT THIS
    return 0
