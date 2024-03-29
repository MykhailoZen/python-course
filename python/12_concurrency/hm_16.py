import random
import time
import concurrent.futures

# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
def calculate_sum(start: int, end: int) -> int:

    list_of_result = [i for i in range(start, end + 1)]
    result = sum(list_of_result)
    return result


# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks,
# obtain the result for each range chunk, and return the total sum. The returning result should be the same as
# for the first function.
def calculate_sum_parallel(start: int, end: int, chunk_size: int = 100000) -> int:
    chunks = [(i, min(i + chunk_size-1, end)) for i in range(start, end + 1, chunk_size)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(calculate_sum, chunk_start, chunk_end) for chunk_start, chunk_end in chunks]
        results = [future.result() for future in futures]

    return sum(results)

# Multithreading, IO-bound work (30 points):
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
def sleep_random():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    return sleep_duration

# Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.
def run_sleep_random():
    start_time = time.time()
    total_workload_time = 0
    max_workload_time = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_random) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            total_workload_time += result
            max_workload_time = max(max_workload_time, result)

    elapsed_time = time.time() - start_time

    return f"Total workload time: {total_workload_time:.2f} seconds,\n" \
           f"Max workload time: {max_workload_time:.2f} seconds,\n" \
           f"Elapsed time: {elapsed_time:.2f} seconds"


if __name__ == "__main__":
    # Verification run calculate_sum()
    start = time.time()
    print("Sequential Sum:", calculate_sum(1, 2**30))
    print("Time spend calculate_sum:", time.time() - start)

    # Verification run calculate_sum_parallel()
    start = time.time()
    print("Parallel Sum:", calculate_sum_parallel(1, 2**30))
    print("Time spend calculate_sum_parallel:", time.time() - start)

    # Verification run sleep_random()
    print("Run sleep random", sleep_random())
    # Verification run run_sleep_random()
    print(run_sleep_random())
