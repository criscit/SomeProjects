from unittest import TestCase

from randomized_algorithms import find_pi


class TestRandomizedAlgorithms(TestCase):
    def test_find_pi(self):
        cases = [100, 1000, 10000, 100000, 1000000]

        for dots in cases:
            with self.subTest(dots=dots):
                pi = find_pi(dots)
                self.assertLess(pi, 4)
                self.assertGreater(pi, 2.5)
