from unittest import TestCase

from simple_recursion import find_recursion_fibonacci


def find_iteration_fibonacci(n: int) -> int:
    # list to store Fibonacci numbers.
    f = []

    # 0th and 1st number of the series are 0 and 1
    f.append(0)
    f.append(1)

    for i in range(2, n+1):
        # Add the previous 2 numbers in the series and store it
        f.append(f[i-1] + f[i-2])

    return f[n]


class TestSimpleRecursion(TestCase):
    def test_find_recursion_fibonacci(self):
        """Find number of Fibonacci."""
        cases = [1, 2, 7, 12]
        for n in cases:
            with self.subTest(n):
                result = find_recursion_fibonacci(n)
                expected_number = find_iteration_fibonacci(n)
                self.assertEqual(result, expected_number)
