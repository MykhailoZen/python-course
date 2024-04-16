from concurrent.futures import ProcessPoolExecutor
import time
import os


def calculate_sum(start, end):
    """Calculates sum of a range of numbers."""
    return sum(range(start, end + 1))


def calculate_sum_parallel(start, end, num_processes=None):
    """Calculates sum of a range of numbers in parallel."""
    if num_processes is None:
        num_processes = os.cpu_count()

    total_numbers = end - start + 1
    chunk_size = total_numbers // num_processes
    remainder = total_numbers % num_processes

    ranges = []
    current_start = start
    for i in range(num_processes):
        current_end = current_start + chunk_size - 1
        if i < remainder:
            current_end += 1
        ranges.append((current_start, current_end))
        current_start = current_end + 1

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        chunk_sums = list(executor.map(lambda args: calculate_sum(*args), ranges))

    return sum(chunk_sums)


if __name__ == '__main__':
    range_start = 1
    range_end = 2 ** 30
    expected_sum = 576460752840294400

    start_time = time.time()
    total_sum_sequential = calculate_sum(range_start, range_end)
    time_sequential = time.time() - start_time
    print(f"Sequential sum: {total_sum_sequential}, Time: {time_sequential}")

    start_time = time.time()
    total_sum_parallel = calculate_sum_parallel(range_start, range_end)
    time_parallel = time.time() - start_time
    print(f"Parallel sum: {total_sum_parallel}, Time: {time_parallel}")

    assert total_sum_parallel == expected_sum, "Parallel sum does not match expected result."
    print("Both methods returned the expected result.")
