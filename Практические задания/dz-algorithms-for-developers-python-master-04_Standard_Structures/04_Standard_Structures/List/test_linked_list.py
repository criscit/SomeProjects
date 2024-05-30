from unittest import TestCase

from linked_list import LinkedList


class TestLinkedList(TestCase):

    def test_to_array(self):
        t1 = [1, 2, 5, 1, 2, 6, 1, 6, 8, 324, -10, 20]
        t2 = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 3]
        self.assertEqual(t1, LinkedList.from_array(t1).to_array())
        self.assertEqual(t2, LinkedList.from_array(t2).to_array())

    def test_get_size(self):
        cases = [
            # source list, expected size
            ([1, 2, 3, 4, 5, 6], 6),
            ([1], 1),
            ([], 0)
        ]
        for (input_list, expected_size) in cases:
            with self.subTest(input_list):
                self.assertEqual(LinkedList.from_array(input_list).get_size(), expected_size)

        self.assertEqual(LinkedList().get_size(), 0)

    def test_every_second(self):
        cases = [
            # Source list, expected list
            ([1, 2, 3, 4, 5, 6], [1, 3, 5]),
            ([1], [1]),
            ([1, 1, 1, 1], [1, 1]),
            ([6, 1, 6, 1, 6, 2, 5, 3, 7], [6, 6, 6, 5, 7])
        ]
        for source, expected in cases:
            with self.subTest(source=source):
                l = LinkedList.from_array(source)
                l2 = l.copy_every_second()
                self.assertEqual(l2.to_array(), expected)

    def test_filter_x(self):
        cases = [
            # source list, divisor, expected list
            ([1, 2, 3, 4, 5, 6], 2, [1, 3, 5]),
            ([1], 7, [1]),
            ([12, 6, 1, 7], 3, [1, 7]),
            ([8, 2, 12, 4, 120, 1240, 5, 1224, 2024], 4, [2, 5]),
            ([], 7, [])
        ]
        for source, divisor, expected in cases:
            with self.subTest(source=source):
                l = LinkedList.from_array(source)
                l.filter_divisible(divisor)
                self.assertEqual(l.to_array(), expected)

    def test_get_and_insert(self):
        l = LinkedList()

        l.push_front(4)
        l.push_front(3)
        l.push_front(1)
        l.insert_after(l.get_at(0), 2)
        l.insert_after(l.get_at(3), 5)
        n = l.get_at(2)
        for _ in range(5):
            l.insert_after(n, 100)

        self.assertEqual(l.to_array(), [1, 2, 3, 100, 100, 100, 100, 100, 4, 5])

    def test_get_and_insert_and_push(self):
        l = LinkedList()

        for _ in range(5):
            l.push_front(0)
            l.insert_after(l.get_at(0), 1)

        self.assertEqual(l.to_array(), [0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
