from typing import List

from item import Item


def readable_difference_between_arrays(expected: List[Item], actual: List[Item]) -> str:
   return " expected:   %s\n actual:     %s\n" % (expected, actual)


class Case:
    def __init__(self, test_array: List[int], compare_to_amount: int):
        self.expected_comparisons = compare_to_amount;
        self.test_array = list(map(Item, test_array))
        self.expected = list(map(Item, sorted(test_array)))

    def __str__(self):
        return str(self.test_array)

class SortMixin:
    def test_sort_and_test_equals_amount(self):
        """Количество сравнений элементов массива."""
        for case in self.cases:
            with self.subTest(case):
                Item.clear_amount_compare_to()
                self.sort(case.test_array)

                compare_to_amount = Item.amount_compare_to
                if case.test_array:
                    val = case.expected_comparisons >= compare_to_amount and compare_to_amount > 0
                else:
                    val = compare_to_amount == 0

                self.assertTrue(
                    val,
                    "\nКоличество проверок элементов превышает достаточное для сортировки или проверки не производились. "
                    + "\nМаксимальное допустимое количество для прохождения теста:%d, количество проверок в коде:%d"
                    % (case.expected_comparisons, compare_to_amount),
                )

    def test_sort(self):
        """Массив отсортирован."""
        for case in self.cases:
            with self.subTest(case):
                self.sort(case.test_array)
                self.assertListEqual(case.test_array, case.expected)
