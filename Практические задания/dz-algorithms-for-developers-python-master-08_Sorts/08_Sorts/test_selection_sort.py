from unittest import TestCase

from selection_sort import sort
from base import Case, SortMixin


class TestSelectionSort(TestCase, SortMixin):
    """Тест Сортировки выборкой / SelectionSort."""
    sort = staticmethod(sort)

    def setUp(self):
        self.cases = [
            Case([1, 2, 3], 3),
            Case([3, 2, 1], 3),
            Case([0, 0, 1, 0, 0], 10),
            Case([-1, -2, 0, 1, 2], 10),
            Case([0], 0),
            Case([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], 55),
        ]
