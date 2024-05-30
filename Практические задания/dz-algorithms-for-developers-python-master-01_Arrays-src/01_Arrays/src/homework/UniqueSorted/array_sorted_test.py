from typing import List
import unittest
from unittest import mock

from array_sorted import group_and_print, crypto_currency_analysis
from printer import print_currency_info, print_phone_info


class ArraySortedTest(unittest.TestCase):
    def test_group_and_print(self):
        """Group phone numbers."""
        numbers = [
            79000000000,
            79000000000,
            79000000001,
            79000000002,
            79000000002,
            79000000003,
            79000000003,
            79000000003,
            79000000003,
            79000000004,
        ]
        with mock.patch('array_sorted.print_phone_info') as mock_print:
            group_and_print(numbers)
            self.assertEqual(mock_print.call_count, 5)

    def test_crypto_currency_analysis(self):
        cases = [
            # Input file, expected calls
            (
                """
                BTC:42
                BTC:600
                BTC:900
                DOGE:123456
                DOGE:69420
                ETH:220
                ETH:666
                XMR:14
                XMR:88
                """,
                [
                    ("BTC", 514.0),
                    ("DOGE", 96438.0),
                    ("ETH", 443.0),
                    ("XMR", 51.0)
                ]
            ), (
                """
                BTC:600
                BTC:600
                BTC:600
                BTC:600
                BTC:600
                BTC:600
                BTC:600
                """,
                [
                    ("BTC", 600.0),
                ]
            ), (
                """
                BTC:1
                DOGE:2
                """,
                [
                    ("BTC", 1.0),
                    ("DOGE", 2.0)
                ]
            ), (
                """
                DOGE:69420
                """,
                [
                    ("DOGE", 69420.0)
                ]
            )
        ]

        for input_file, expectedCalls in cases:
            with self.subTest(input_file=input_file):
                with mock.patch('array_sorted.print_currency_info') as mock_print:
                    crypto_currency_analysis(input_file)
                    mock_print.assert_has_calls([mock.call(*args) for args in expectedCalls])
