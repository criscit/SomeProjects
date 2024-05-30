from typing import List
import time
from random import randint

from example import find_unique


def generate_random(size: int) -> List[int]:
    arr = [None] * size
    for i in range(size):
        arr[i] = randint(1, 2 ** 32)

    return arr


if __name__ == '__main__':
    total_unique = 0

    # Make it like 30-50 for faster results,
    # 100 iterations may take ~5-10 minutes
    total_iterations = 100
    sizes, durations = [], []
    size = 100

    print("Running %d iterations,\n_hang on, this will take a while..." % total_iterations)
    for i in range(total_iterations):
        test_array = generate_random(size)
        start = time.monotonic()
        unique = find_unique(test_array)
        duration = time.monotonic() - start

        sizes.append(size)
        durations.append(duration)
        total_unique += len(unique)
        size += 100

        print("(%d/%d) find_unique([%d elements]) took %f seconds" % (i, total_iterations, size, duration))

    print("Total unique numbers = %d" % total_unique)
