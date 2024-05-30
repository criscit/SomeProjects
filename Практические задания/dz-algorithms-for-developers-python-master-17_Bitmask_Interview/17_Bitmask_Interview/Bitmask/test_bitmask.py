from unittest import TestCase
import random

from bitmask import is_submask, rotate


class TestBitmask(TestCase):
    def test_is_submask(self):
        for i in range(1000):
            a = [random.randint(0, 255) for _ in range(4)]
            b = [random.randint(0, 255) for _ in range(4)]
            f = True
            for aj, bj in zip(a, b):
                if aj & bj != bj:
                    f = False

            if random.randint(0, 1):
                f = True
                for j in range(4):
                    b[j] &= a[j]

            s1 = '.'.join(map(str, a))
            s2 = '.'.join(map(str, b))

            self.assertEqual(f, is_submask(s1, s2))

    def test_rotate(self):
        for i in range(10000):
            x = random.randint(-10000, 10000)
            c = random.randint(0, 199)
            ex = x
            if c > 0:
                for j in range(c):
                    ex = rotl(ex)
            else:
                for j in range(-c):
                    ex = rotr(ex)

            self.assertEqual(ex, rotate(x, c))


def rotr(x: int) -> int:
    c = x & 1
    x = x >> 1
    x = x | (c << 31)
    return x


def rotl(x: int) -> int:
    c = x >> 31
    x = x << 1
    x = ((x | 1) ^ 1) ^ c
    return x
