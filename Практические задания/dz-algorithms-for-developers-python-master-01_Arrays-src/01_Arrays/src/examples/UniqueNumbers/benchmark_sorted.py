from typing import List
import time
from random import randint

from example_sorted import find_unique_sorted


def generate_random_sorted(size: int) -> List[int]:
    arr = [None] * size
    for i in range(size):
        arr[i] = randint(1, 2 ** 32)

    arr.sort()
    return arr


if __name__ == '__main__':
    total_unique = 0

    # Make it like 300-500 for faster results,
    # 1000 iterations may take ~5-10 minutes
    total_iterations = 1000
    sizes, durations = [], []
    size = 1000

    print("Running %d iterations,\n_hang on, this will take a while..." % total_iterations)
    for i in range(total_iterations):
        test_array = generate_random_sorted(size)
        start = time.monotonic()
        unique = find_unique_sorted(test_array)
        duration = time.monotonic() - start

        sizes.append(size)
        durations.append(duration)
        total_unique += len(unique)
        size += 5000

        print("(%d/%d) find_unique_sorted([%d elements]) took %f seconds" % (i, total_iterations, size, duration))

    print("Total unique numbers = %d" % total_unique)
