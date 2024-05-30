from unittest import TestCase

import matrix


class TestMatrix(TestCase):
    def test_paint(self):
        matrix1 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
        target_matrix1 = [[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0]]
        matrix2 = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]]
        target_matrix2 = [[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]

        cases = [
            (matrix1, 0, 1, 1, target_matrix1),
            (matrix2, 0, 3, 1, target_matrix2),
        ]

        for matrix, row, col, new_color, expected in cases:
            with self.subTest(matrix=matrix):
                actual = matrix.paint(matrix, row, col, new_color)
                self.assertEqual(actual, expected)

    def test_num_islands(self):
        grid1 = [
                ['1', '1', '1', '1', '0'],
                ['1', '1', '0', '1', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '0', '0', '0']
        ]
        self.assertEqual(matrix.num_islands(grid1), 1)

        grid2 = [
                ['1', '1', '0', '0', '0'],
                ['1', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '0'],
                ['0', '0', '0', '1', '1']
        ]
        self.assertEqual(matrix.num_islands(grid2), 3)
