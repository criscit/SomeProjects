from unittest import TestCase

import courses


class TestCources(TestCase):
    def test_can_finish(self):
        cases = [
            (2, [[1,0]], True),
            (2, [[1,0], [0,1]], False),
            (5, [[4,3], [3,2], [2,1], [1,0]], True),
        ]
        for num_courses, prerequisites, expected in cases:
            with self.subTest(num_courses=num_courses, prerequisites=prerequisites, expected=expected):
                actual = courses.can_finish(num_courses, prerequisites)
                self.assertEqual(actual, expected)
