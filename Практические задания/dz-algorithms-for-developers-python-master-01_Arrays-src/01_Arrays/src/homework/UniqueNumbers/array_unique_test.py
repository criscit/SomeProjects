from typing import List
import unittest
from unittest import mock

from array_unique import letters_learned_today, avoid_jail_due_to_tax_fraud


class ArrayUniqueTest(unittest.TestCase):
    def test_letters_learned_today(self):
        """Learning letters."""
        cases = [
            ("АААФФФФФФФЖЫЫЫЫБЫРВАААААЛГГГХЫХЫБЛИА", "АФЖЫБРВЛГХИ"),
            ("ОК", "ОК"),
            ("СКИЛЛБОКСТОПЧИК", "СКИЛБОТПЧ"),
            ("ААААААААА", "А"),
        ]

        for word, expected in cases:
            with self.subTest(word=word):
                actual = letters_learned_today(word)
                self.assertEqual(actual, expected)

    def test_avoid_jail_due_to_tax_fraud(self):
        """Avoiding jail due to tax fraud."""
        cases = [
            # tuple values are: report, expected
            (
                [
                    [12391203, 3828382, 334934939],
                    [45345345, 5341312, 55345345],
                    [334934939, 1234122, 657657],
                ],
                334934939
            ),
            (
                [
                    [1, 1, 1],
                    [1, 1, 1]
                ],
                1
            ),
            (
                [
                    [1, 2, 3],
                    [4, 5, 6],
                ],
                -1
            ),
        ]
        for i, (report, expected) in enumerate(cases):
            with self.subTest(f"Example #{i}"):
                actual = avoid_jail_due_to_tax_fraud(report)
                self.assertEqual(actual, expected)
