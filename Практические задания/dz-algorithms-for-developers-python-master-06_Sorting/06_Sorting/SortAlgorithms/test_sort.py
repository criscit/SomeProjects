import unittest
from typing import List
from time import perf_counter
from random import randint

import bubble_sort, selection_sort, counting_sort, insertion_sort
from super_array import SuperArray
from animal import Animal


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        cases = [
            [334934939, 1234122, 657657],
            [],
            [randint(0, 2 ** 32) for _ in range(10000)]
        ]
        for i, array in enumerate(cases):
            with self.subTest(f'array{i}'):
                expected_array = sorted(array)
                bubble_sort.sort(array)
                self.assertListEqual(expected_array, array)

    def test_selection_sort(self):
        cases = [
            [3, 2, 1],
            [],
            list(range(100, 0, -1)),
        ]
        for array in cases:
            with self.subTest(array):
                expected_array = sorted(array)
                super_array = Arr(array.copy())
                selection_sort.sort(super_array)
                self.assertListEqual(expected_array, super_array.array)
                print(expected_array)
                self.assertEqual(super_array.iteration, len(array) * 2)

    def test_insertion_sort(self):
        animals = [
            ZooAnimal(100, "Zebra Fibi"),
            ZooAnimal(505, "Lion Gunter"),
            ZooAnimal(5, "Meerkat Joe"),
            ZooAnimal(100, "Zebra Monika"),
            ZooAnimal(50, "Deer Ross"),
            ZooAnimal(5, "Meerkat Chandler")
        ]
        expected_animals = animals.copy()
        ZooAnimal.sort(expected_animals)

        insertion_sort.sort(animals)

        self.assertEqual(animals, expected_animals)

    def test_counting_sort(self):
        arr = [randint(1, 100) for _ in range(1000000)]
        arr2 = arr.copy()

        start = perf_counter()
        arr = quicksort(arr)
        quicksort_time = perf_counter() - start

        start = perf_counter()
        counting_sort.sort(arr2, 100)
        counting_sort_time = perf_counter() - start

        self.assertListEqual(arr, arr2)
        self.assertGreater((quicksort_time / counting_sort_time),  2)
        # не очень честно сравнивать создание новых списков против inplace сортировки
        # но тут как-то иного выхода и нет, quicksort in place не "помещается" в рамки позволенной по
        # умолчанию глубины рекурсии


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


class Arr(SuperArray):
    def __init__(self, array: List[int]):
        self.iteration = 0
        self.array = array

    def get_size(self) -> int:
        return len(self.array)

    def get(self, position: int) -> int:
        return self.array[position]

    def set(self, position: int, value: int) -> None:
        self.iteration += 1
        self.array[position] = value


class ZooAnimal(Animal):
    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name

    def get_weight(self) -> int:
        return self.weight

    def __eq__(self, other: "Animal") -> bool:
        return self.weight == other.weight and self.name == other.name

    def __repr__(self):
        return "ZooAnimal{weight=" + str(self.weight) + ", name='" + self.name + "'" + '}'

    @staticmethod
    def sort(arr: List[Animal]) -> None:
        for left in range(len(arr)):
            value = arr[left]
            i = left - 1
            while i >= 0:
                if value.get_weight() < arr[i].get_weight():
                    arr[i+1] = arr[i]
                else:
                    break
                i -= 1
            arr[i+1] = value
