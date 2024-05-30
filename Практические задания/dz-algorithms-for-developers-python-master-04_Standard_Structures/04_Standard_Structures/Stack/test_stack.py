from unittest import TestCase

from stack import calc_polish


class TestStack(TestCase):
    def test_calc_polish(self):
        cases = [
            # polish_str, expected output
            ("8 9 + 1 7 - *", -102),
            ("9 9 9 9 9 9 9 9 9 * * * * * * * *", 387420489),
            ("2 3 4 5 * 6 - 7 + 8 9 2 * 3 4 1 - 3 4 + * 5 - + * + - * +", -985),
            ("1 2 - 1 2 3 4 5 6 7 8 9 * * * * * * * * * 9 8 7 6 * * * *", -1097349120),
            ("1234", 1234),
            ("-1234", -1234),
            ("1234 1 1 + +", 1236),
        ]

        for (polish_str, expected_result) in cases:
            with self.subTest(polish_str):
                self.assertEqual(calc_polish(polish_str), expected_result)

    def test_calc_polish_long(self):
        # long string cases
        cases = []

        # First case
        b = ""
        s = 0
        for i in range(1, 10000):
            s += i
            b += str(i) + " "
        for i in range(1, 10000):
            b += "+"
            if i != 9999:
                b += " "
        cases.append(("long_polish_str1", b, (10000 * 9999) / 2))

        # Second case
        b = ""
        b += "0 "
        for i in range(1, 20000):
            b += str(i) + " +"
            if i != 19999:
                b += " "
        cases.append(("long_polish_str2", b, (20000 * 19999) / 2))

        for (name, polish_str, expected_result) in cases:
            with self.subTest(name):
                self.assertEqual(calc_polish(polish_str), expected_result, "No match")
