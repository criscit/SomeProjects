from unittest import TestCase

from compress_work import compress, decompress, remove_comments


class TestMatrix(TestCase):
    def test_provider_compress(self):
        """Compress graduated work."""
        cases = [("aaaabbbc", "a4b3c1"), ("a", "a1"), ("", ""), ("asdfggh", "a1s1d1f1g2h1")]
        for graduated_work, compressed_graduated_work in cases:
            with self.subTest(graduated_work=graduated_work):
                actual = compress(graduated_work)
                self.assertEqual(actual, compressed_graduated_work)

    def test_decompress(self):
        """Decompress graduated work."""
        cases = [("aaaabbbc", "a4b3c1"), ("a", "a1"), ("", ""), ("asdfggh", "a1s1d1f1g2h1")]
        for graduated_work, compressed_graduated_work in cases:
            with self.subTest(compressed_graduated_work=compressed_graduated_work):
                actual = decompress(compressed_graduated_work)
                self.assertEqual(actual, graduated_work)

    def test_remove_comments(self):
        """Delete comments from work."""
        source = [
            "/*Test program */",
            "public static void main(String[] args) {",
            "  // variable declaration ",
            "int b = 2;",
            "int c = 3;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing input */",
            "System.out.println(b + c);",
            "}",
        ]
        expected = [
            "public static void main(String[] args) {",
            "int b = 2;",
            "int c = 3;",
            "System.out.println(b + c);",
            "}",
        ]

        actual = remove_comments(source)
        self.assertEqual(actual, expected)
