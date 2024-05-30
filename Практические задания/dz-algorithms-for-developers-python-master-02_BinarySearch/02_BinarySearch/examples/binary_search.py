from typing import List


def binary_search(array: List[int], search: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] < search:
            left = middle + 1
        elif array[middle] > search:
            right = middle - 1
        else:
            return middle

    return -1
