"""
1. Multiprocessing, CPU-bound work (30 points):
- Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.
- Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
Split the given range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be the same as for the first function.
- Print the times it takes for each approach.
"""

import time
import multiprocessing
import math


def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

def calculate_sum_parallel(start: int, end: int, n_proc = multiprocessing.cpu_count()) -> int:
    num_range = end - start + 1
    chunk_size = int(num_range / n_proc)
    n_chunks = math.ceil(num_range / chunk_size)
    ranges = []
    left = start
    for i in range(0, n_chunks):
        right = min(end, left + chunk_size - 1)
        ranges.append((left, right))
        left += chunk_size
    with multiprocessing.Pool(n_proc) as p:
        return sum(p.starmap(calculate_sum, ranges))

if __name__ == '__main__':
    n = 2**30
    start_time = time.time()
    print(calculate_sum(1, n))
    duration = time.time() - start_time
    print(f'{duration} secs of first method')
    start_time = time.time()
    print(calculate_sum_parallel(1, n))
    duration = time.time() - start_time
    print(f'{duration} secs of second method')

