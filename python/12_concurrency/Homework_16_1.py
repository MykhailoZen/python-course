# Multiprocessing, CPU-bound work
import time
from concurrent.futures import ProcessPoolExecutor


def calculate_sum(start: int, end: int) -> int:
    return ((end - start + 1) * (start + end)) // 2


def calculate_sum_wrapper(args):
    return calculate_sum(*args)


def calculate_sum_parallel(start: int, end: int, chunks: int) -> int:
    chunk_size = (end - start) // chunks + 1
    ranges = [(start + i * chunk_size, min(end, start + (i + 1) * chunk_size - 1)) for i in range(chunks)]

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(calculate_sum_wrapper, ranges))

    return sum(results)


if __name__ == "__main__":
    range_start, range_end = 1, 2 ** 30
    expected_result = 576460752840294400

    start_time = time.time()
    result_sequential = calculate_sum(range_start, range_end)
    end_time = time.time()
    print(f"Sequential calculation result: {result_sequential}, Time taken: {end_time - start_time:.2f} seconds.")
    assert result_sequential == expected_result, "Sequential calculation did not match the expected result."

    start_time = time.time()
    result_parallel = calculate_sum_parallel(range_start, range_end, chunks=8)
    end_time = time.time()
    print(f"Parallel calculation result: {result_parallel}, Time taken: {end_time - start_time:.2f} seconds.")
    assert result_parallel == expected_result, "Parallel calculation did not match the expected result."
