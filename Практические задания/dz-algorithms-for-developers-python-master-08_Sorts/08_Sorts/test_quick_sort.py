from unittest import TestCase

from quick_sort import sort
from base import Case, SortMixin


class TestBubbleSort(TestCase, SortMixin):
    sort = staticmethod(sort)

    def setUp(self):
        self.cases = [
            Case([1, 2, 3], 4),
            Case([3, 2, 1], 4),
            Case([0, 0, 1, 0, 0], 15),
            Case([-1, -2, 0, 1, 2], 11),
            Case([0], 0),
            Case([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], 36),
            Case([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40], 48),
        ]
