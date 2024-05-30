import unittest

from array_max import (
    find_smallest_transaction, find_best_student_mistakes, find_average_time, find_most_profitable_client
)


class ArrayMaxTest(unittest.TestCase):
    def test_find_smallest_transaction(self):
        """Finding smallest transaction."""
        cases = [
            [-1000, -100, -10, -1],
            [-1000],
            [-1000, -100, -10, -1, -1],
            [-1000, -100, -10, -1, -1, 0],
            [- 2 ** 32]
        ]

        for array in cases:
            with self.subTest(array):
                actual = find_smallest_transaction(array)
                array.sort()
                expected = array[-1]
                self.assertEqual(expected, actual)

    def test_find_best_student_mistakes(self):
        """Finding best student."""
        cases = [
                [9, 4, 1, 8, 7, 13, 6, 5],
                [1000],
                [9, 4, 1, 8, 7, 13, 6, 5, 1, 1, 1, 1, 1],
                [9, 4, 1, 8, 7, 13, 6, 5, 0],
                [2 ** 32]
        ]
        for array in cases:
            with self.subTest(array):
                actual = find_best_student_mistakes(array)
                array.sort()
                expected = array[0]
                self.assertEqual(expected, actual)

    def test_find_average_time(self):
        """Finding average time."""
        cases = [
            [9999],
            [9, 4, 1, 8, 7, 9, 4, 1, 8, 7, 8, 7, 18, 3, 13, 6, 5],
            [2 ** 32, 2 ** 32, 2 ** 32, 2 ** 32, 2 ** 32]
        ]
        for array in cases:
            with self.subTest(array):
                actual = find_average_time(array)
                expected = sum(array) / len(array)
                self.assertAlmostEqual(expected, actual, delta=0.1)

    def test_find_most_profitable_client(self):
        """Finding most profitable client."""
        cases = [
            # tuple values are: array, expected index
            (
                [
                    [11, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [12, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [13, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [14, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [15, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [16, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [17, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [18, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [19, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                    [10, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                ],
                8,
            ), (
                [
                    [1, 2 ** 32, -2 ** 32],
                    [1, 2, 3],
                ],
                1
            ), (
                [
                    [1, 9999, -10],
                    [1],
                ],
                0
            ), (
                [
                    [95, 67, 13, 55, 44, 11, 10],
                    [7, 190, 4, 44, 11, 1, 99],
                    [0, 5, -1, 500, 14, 90, 1],
                ],
                2
            )
        ]
        for i, (arrays, expected) in enumerate(cases):
            with self.subTest(f"Example {i}"):
                actual = find_most_profitable_client(arrays)

                self.assertEqual(actual, expected)
