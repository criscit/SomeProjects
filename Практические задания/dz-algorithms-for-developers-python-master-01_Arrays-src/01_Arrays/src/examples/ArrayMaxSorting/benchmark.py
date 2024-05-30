from typing import List
from random import randint
import time


def generate_random_sorted(size: int) -> List[int]:
    arr = [None] * size
    for i in range(size):
        arr[i] = randint(1, 2 ** 32)

    arr.sort()


count = 10000000
arr: List[int] = []
for _ in range(count):
    arr.append(randint(1, 2 ** 16))

start_time = time.monotonic()
arr.sort()
duration = time.monotonic() - start_time
# String.format()
print("It took %.3f seconds to sort %d elements" % (duration, count))
print("Sorted: [ %d, %d, ... %d, %d ]" % (arr[0], arr[1], arr[len(arr)-2], arr[len(arr)-1]))
