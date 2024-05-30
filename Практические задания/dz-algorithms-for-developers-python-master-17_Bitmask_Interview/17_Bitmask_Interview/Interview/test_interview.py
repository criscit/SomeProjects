from typing import List
from unittest import TestCase
from functools import partial
from copy import deepcopy
import random

from interview import find_subarray, rotate_matrix


randint = partial(random.randrange, -2 ** 32, 2 ** 32)


class TestInterview(TestCase):
    @staticmethod
    def slow_solve1(a: List[int], S: int) -> bool:
        """
        Это медленное решение, вы должны придумать решение, которое работает за О(N)
        И вообще, подсматривать решения в тестах - нехорошо :)
        """
        for i in range(len(a)):
            s = 0
            for j in range(i, len(a)):
                s += a[j]
                if s == S:
                    return True
        return False

    @staticmethod
    def slow_solve2(a: List[List[int]]):
        """
        Это медленное решение, вы должны придумать решение, которое не использует доп массив
        И вообще, подсматривать решения в тестах - нехорошо
        """
        l = len(a)
        b = [[0] * l for _ in range(l)]
        for i in range(l):
           for j in range(l):
               b[l-j-1][i] = a[i][j]

        for i in range(l):
            for j in range(l):
                a[i][j] = b[i][j]

    def test_find_subarray(self, times=100):
        for _ in range(times):
            n = random.randrange(10, 10010)
            a = [random.randrange(-500,500) for _ in range(n)]
            l = random.randrange(0, n)
            r = random.randrange(0, n)
            if r < l:
                l, r = r, l

            s = 0
            for i in range(l, r+1):
                s += a[i]

            self.assertEqual(self.slow_solve1(a, s), find_subarray(a, s))

        cnt = 0
        for _ in range(times):
            n = random.randrange(10, 10010)
            a = [random.randrange(-500,500) for _ in range(n)]
            l = random.randrange(0, n)
            r = random.randrange(0, n)
            if r < l:
                l, r = r, l
            s = random.randrange(-10000, 10000)
            if not self.slow_solve1(a, s):
                cnt += 1

            self.assertEqual(self.slow_solve1(a, s), find_subarray(a, s))

    def test_rotate_matrix(self, times=100):
        for _ in range(times):
            n = random.randrange(1, 101)

            a = [[randint() for _ in range(n)] for _ in range(n)]
            b = deepcopy(a)

            self.slow_solve2(a)
            rotate_matrix(b)
            self.assertEqual(a, b)
