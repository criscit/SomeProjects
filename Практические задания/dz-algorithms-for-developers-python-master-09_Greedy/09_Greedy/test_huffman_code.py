from unittest import TestCase

from huffman_code import encode_huffman


class HuffmanCodeTest(TestCase):
    def test_huffman_encode(self):
        """Huffman encode."""
        cases = [
            # text, result
            ("", 0),
            ("a", 1),
            ("aa", 3),
            ("b", 1),
            ("aba", 5),
            ("aaa", 7),
            ("Skillbox", 2269627),
            ("abcdefg", 640693)
        ]
        for text, result in cases:
            with self.subTest(text=text):
                self.assertEqual(encode_huffman(text), result)
