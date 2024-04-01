import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count


def calculate_sum(start: int, end: int) -> int:
    """Calculates the sum of numbers in the given range (inclusive)."""
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


def calculate_sum_parallel(start: int, end: int) -> int:
    """Calculates the sum of numbers in the given range (inclusive) in parallel."""
    chunk_size = (end - start + 1) // cpu_count()
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    with ProcessPoolExecutor() as executor:
        partial_sums = executor.map(calculate_sum, [chunk_start for chunk_start, _ in chunks],
                                    [chunk_end for _, chunk_end in chunks])
    return sum(partial_sums)


if __name__ == "__main__":
    target_range = (1, 2 ** 30)
    expected_sum = 576460752840294400

    start_time = time.time()
    single_process_sum = calculate_sum(*target_range)
    end_time = time.time()
    single_process_time = end_time - start_time

    start_time = time.time()
    parallel_sum = calculate_sum_parallel(*target_range)
    end_time = time.time()
    parallel_time = end_time - start_time

    assert single_process_sum == expected_sum
    assert parallel_sum == expected_sum

    print(f"Single process sum: {single_process_sum}")
    print(f"Single process time: {single_process_time:.4f} seconds")
    print(f"Parallel sum: {parallel_sum}")
    print(f"Parallel time: {parallel_time:.4f} seconds\n\n")
