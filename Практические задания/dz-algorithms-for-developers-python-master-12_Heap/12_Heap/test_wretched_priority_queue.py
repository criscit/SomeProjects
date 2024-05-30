from typing import Set, List
from time import perf_counter
from unittest import TestCase
import random
import heapq, math

from wretched_priority_queue import WretchedPriorityQueue, NoSuchElementException

SIZE = 500


class WretchedPriorityQueueTest(TestCase):
    def test_size(self):
        queue = WretchedPriorityQueue()
        self.assertEqual(0, queue.size)

        queue.add(1)
        self.assertEqual(1, queue.size)

        queue.pop()
        self.assertEqual(0, queue.size)

    def test_is_empty(self):
        queue = WretchedPriorityQueue()
        self.assertTrue(queue.is_empty())

        queue.add(1)
        self.assertFalse(queue.is_empty())

        queue.pop()
        self.assertTrue(queue.is_empty())

    def test_peek(self):
        queue = WretchedPriorityQueue()
        for i in range(1, SIZE+1):
            queue.add(i)

        for i in range(SIZE, 0, -1):
            self.assertEqual(SIZE - i + 1, queue.peek())
            self.assertEqual(SIZE - i + 1, queue.pop())

        with self.assertRaises(NoSuchElementException):
            queue.peek()

    def test_pop(self):
        ints = []
        queue = WretchedPriorityQueue()
        for i in range(100):
            x = random.randint(-10000, 10000)
            heapq.heappush(ints, x)
            queue.add(x)

        while ints:
            self.assertEqual(heapq.heappop(ints), queue.pop())

        with self.assertRaises(NoSuchElementException):
            queue.peek()

    def test_time(self):
        ints = []
        queue = WretchedPriorityQueue()
        a = {random.randint(-1000000, 1000000) for _ in range(1000)}

        start = perf_counter()
        for k in a:
            heapq.heappush(ints, k)
        while ints:
            heapq.heappop(ints)
        standart = perf_counter() - start

        start = perf_counter()
        for k in a:
            queue.add(k)
        while not queue.is_empty():
            i = queue.pop()
        our = perf_counter() - start

        self.assertLess(our/standart, 10, "Очередь работает слишком долго")
