import hashlib
from unittest import TestCase

from hash import decrypt, encrypt, same_5last_chars


class TestHash(TestCase):
    def test_encrypt(self):
        """Encrypt password."""
        cases = [
            ("google.com", "Skillbox", "EmrWiux20NoKOxooGDs5zA=="),
            ("Hello world!", "qwerty", "DPTIhvuQAx2kJqSwBVRw2g=="),
            ("Present", "simsalabim", "GbWZcIfkfyBE2ejJZlGbSQ==")
        ]
        for str_to_encrypt, secret, expected in cases:
            with self.subTest(str_to_encrypt=str_to_encrypt):
                actual = encrypt(str_to_encrypt, secret)
                self.assertEqual(actual, expected)

    def test_same_5last_chars(self):
        """Find strings with the same last 5 chars."""
        result = same_5last_chars()
        self.assertIsNotNone(result)

        first_hash = md5(result[0])
        second_hash = md5(result[1])

        self.assertEqual(first_hash[:-5], second_hash[:-5])

    def test_decrypt(self):
        cases = [
            ("EmrWiux20NoKOxooGDs5zA==", "Skillbox", "google.com"),
            ("DPTIhvuQAx2kJqSwBVRw2g==", "qwerty", "Hello world!"),
            ("GbWZcIfkfyBE2ejJZlGbSQ==", "simsalabim", "Present"),
        ]
        for str_to_decrypt, secret, expected in cases:
            with self.subTest(str_to_decrypt=str_to_decrypt):
                actual = decrypt(str_to_decrypt, secret)
                self.assertEqual(actual, expected)


def md5(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()
