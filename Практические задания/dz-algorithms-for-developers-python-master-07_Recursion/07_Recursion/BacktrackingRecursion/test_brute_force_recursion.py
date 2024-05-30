from unittest import TestCase
from typing import List, Optional

from simple_recursion import find_recursion_fibonacci
from brute_force_recursion import order_of_release_features, check_powers_of_three, possible_messages


class TestBruteForceRecursion(TestCase):
    def test_order_of_release_features(self):
        """Find all possible order of release features."""
        l1 = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]

        l2 = [
            [13, 21],
            [21, 13],
        ]

        l3 = [
            [98],
        ]

        cases = [
            ([1, 2, 3], l1),
            ([13, 21], l2),
            ([98], l3),
        ]
        for numbers_of_features, expected_release_features:
            with self.subTest(numbers_of_features):
                actual = order_of_release_features(numbers_of_features)
                self.assertListEqual(actual, expected_release_features)

    def test_check_powers_of_three_test(self):
        """Help Ivan check powers of 3."""
        cases = [
            (12, True),
            (11, False),
            (91, False),
            (112, True),
        ]
        for number, expected_result in cases:
            with self.subTest(number):
                actual = check_powers_of_three(number)
                self.assertEqual(actual, expected_result)

    def test_possible_messages_test(self):
        """Find possible messages."""
        cases = [
            ("", []),
            ("2", ["a", "b", "c"]),
            ("43", ["gd", "ge", "gf", "hd", "he", "hf", "id", "ie", "if"]),
            ("239", ["adw", "adx", "ady", "adz",
                    "aew", "aex", "aey", "aez",
                    "afw", "afx", "afy", "afz",
                    "bdw", "bdx", "bdy", "bdz",
                    "bew", "bex", "bey", "bez",
                    "bfw", "bfx", "bfy", "bfz",
                    "cdw", "cdx", "cdy", "cdz",
                    "cew", "cex", "cey", "cez",
                    "cfw", "cfx", "cfy", "cfz"]),
        ]
        for number, expected_messages:
            with self.subTest(number):
                actual = possible_messages(number)
                self.assertEqual(actual, expected_messages)
