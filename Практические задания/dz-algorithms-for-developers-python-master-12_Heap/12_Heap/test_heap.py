from typing import Set, List
from unittest import TestCase
import random
import heapq, math

import heap

class HeapTest(TestCase):
    def test_build_heap(self):
        """Heap build."""
        cases = [
            [1, 2, -1],
            [],
            [1],
            [random.randint(0, 10000) for _ in range(100)]
        ]
        for arr in cases:
            with self.subTest(arr=arr):
                heap.build_heap_from_array(arr)
                self.assertIsHeap(arr)

    def assertIsHeap(self, arr):
        n = len(arr) - 1
        for i in range((n-2) // 2):
            if arr[2*i + 1] > arr[i]:
                raise AssertionError("not a heap")
            if arr[2*i + 2] < n and arr[2*i + 2] > arr[i]: 
                raise AssertionError("not a heap")

    def test_k_closest_trucks(self):
        """Find trucks."""
        cases = [
            [1, 1],
            [100, 5],
            [1000, 5],
            [10, 500],
            [10_000, 500]
        ]
        for count, k in cases:
            with self.subTest(count=count, k=k):
                lst = [heap.TruckCoordinate(random.randint(-1000, 1000), random.randint(-1000, 1000)) for _ in range(count)]
                ans = heap.k_closest_trucks(lst, k)
                expected = heapq.nsmallest(k, lst, key=lambda item: math.sqrt(item.x**2 + item.y**2))
                self.assertListEqual(ans, expected)

    def test_unloading_trucks(self):
        """Unloading trucks."""
        n = random.randint(0, 50)
        lst = [random.randint(1, 999) for _ in range(random.randint(0, 1000))]
        ans = heap.unloading_truck(n, lst)
        expected = self.handle_trucks(n, lst)

        self.assertEqual(ans, expected)

    def handle_trucks(self, n: int, tasks: List[int]):
        class TruckTime:
            """Prioritized item."""
            counter = 0
            def __init__(self):
                self.id = TruckTime.counter
                self.time = 0
                TruckTime.counter += 1

            def __lt__(self, other):
                if self.time == other.time:
                    return self.id < other.id
                return self.time < other.time

        queue = [TruckTime() for _ in range(n)]
        records = []
        for task in tasks:
            truck_time = heapq.heappop(queue)
            records.append(truck_time.time)
            truck_time.time += task
            heapq.heappush(queue, truck_time)

        return records
