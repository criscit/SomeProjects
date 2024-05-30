from unittest import TestCase

from insertion_sort import sort
from base import Case, SortMixin


class TestInsertionSort(TestCase, SortMixin):
    sort = staticmethod(sort)

    def setUp(self):
        self.cases = [
            Case([1, 2, 3], 2),
            Case([3, 2, 1], 3),
            Case([0, 0, 1, 0, 0], 6),
            Case([-1, -2, 0, 1, 2], 4),
            Case([0], 0),
            Case([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], 55),
        ]
