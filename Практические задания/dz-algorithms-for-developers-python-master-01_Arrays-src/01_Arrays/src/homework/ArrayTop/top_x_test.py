import unittest

from top_x import find_top_elements, find_bottom_elements


class TextTopX(unittest.TestCase):

    def test_find_top_elements_doesnt_raise(self):
        cases = [
            # Это только один из примеров, при которых код не работает
            # Вам нужно найти еще!
            ([10, 20, 30, 40], -1),
        ]
        for array, number_of_elements in cases:
            with self.subTest(array=array):
                find_top_elements(array, number_of_elements)

    def test_find_bottom_elements(self):
        cases = [
            ([40, 50, 60, 10, 20, 30, 70, 80], 3)
        ]
        for array, number_of_elements in cases:
            with self.subTest(array=array):
                find_bottom_elements(array, number_of_elements)

    def test_find_top_elements_with_repeating(self):
        cases = [
                ([100, 100, 100, 55, 8], 3),
                ([100, 100, 100, 55, 8], 2),
                ([100, 55, 8, 100, 100], 4),
                ([0, 0, 0, 0], 4)
        ]
        for array, number_of_elements in cases:
            with self.subTest(case=(array, number_of_elements)):
                res = find_top_elements(array, number_of_elements)
                self.assertListEqual(res, sorted(array, reverse=True)[:number_of_elements])
