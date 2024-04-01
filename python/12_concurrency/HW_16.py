import multiprocessing
import time
import random
import concurrent.futures


# Multiprocessing, CPU-bound work (30 points):
# 1. Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

# 2. Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum"
# in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.

def calculate_sum_parallel(start: int, end: int, chunk_size: int = 10000) -> int:
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.starmap(calculate_sum, chunks)

    return sum(result)


# Multithreading, IO-bound work (30 points):
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

def wast_time():
    sleep_time = random.uniform(1, 10)
    time.sleep(sleep_time)
    return sleep_time

# Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.
# (optional) asyncio practice: Implement the multithreading task above using the asyncio approach.

def parallel_wast_time():
    total_workload = 0
    max_workload = 0

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = [pool.submit(wast_time) for i in range(20)]

        for future in concurrent.futures.as_completed(futures):
            sleep_time = future.result()
            total_workload += sleep_time
            max_workload = max(max_workload, sleep_time)

    end_time = time.time()
    elapsed_time = end_time - start_time
    return total_workload, max_workload, elapsed_time


if __name__ == '__main__':
    print("Example of Multiprocessing, CPU-bound work:\n")
    # 3. Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
    # Print the times it takes for each approach.
    start_time = time.time()
    result_sequential = calculate_sum(1, 2 ** 30)
    sequential_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2 ** 30)
    parallel_time = time.time() - start_time

    print(f"calculating the sum of numbers sequentially: \n{result_sequential}")
    print(f"execution time of calculating the sum of numbers sequentially: \n{sequential_time} sec")
    print(f"calculating the sum of numbers parallel: \n{result_parallel}")
    print(f"execution time of calculating the sum of parallel: \n{parallel_time} sec")

    if result_sequential == result_parallel == 576460752840294400:
        print("Calculated result the same.\n")


    print("Example of Multithreading, IO-bound work:\n")
    total_workload, max_workload, elapsed_time = parallel_wast_time()
    print(f"Total workload (sum of results of all calls):\n{total_workload} sec")
    print(f"Maximum workload (longest task):\n{max_workload} sec")
    print(f"Total elapsed task execution time:\n{elapsed_time} sec")