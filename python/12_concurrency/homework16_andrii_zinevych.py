import multiprocessing
import time


def calculate_sum(start: int, end: int) -> int:

    return sum(range(start, end + 1))


def calculate_sum_parallel(start: int, end: int, num_processes: int = None) -> int:

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    chunk_size = (end - start + 1) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    results = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_processes - 1 else end
        results.append(pool.apply_async(calculate_sum, (chunk_start, chunk_end)))

    pool.close()
    pool.join()

    total_sum = sum(result.get() for result in results)
    return total_sum




def main():
    start = 1
    end = 2 ** 30

    # Run the sequential function
    print("Running sequential function...")
    start_time = time.time()
    result_sequential = calculate_sum(start, end)
    end_time = time.time()
    sequential_time = end_time - start_time
    print("Sequential result:", result_sequential)
    print("Sequential execution time:", sequential_time, "seconds")

    # Run the parallel function
    print("\nRunning parallel function...")
    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    end_time = time.time()
    parallel_time = end_time - start_time
    print("Parallel result:", result_parallel)
    print("Parallel execution time:", parallel_time, "seconds")

    # Verify the results
    expected_result = 576460752840294400
    assert result_sequential == result_parallel == expected_result, "Results do not match"
    print("\nResults match!")


if __name__ == "__main__":
    main()
