# Multiprocessing, CPU-bound work (30 points):
# 1.Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers
# in the given range including both ends.
import multiprocessing
import time
import concurrent.futures
import random


def calculate_sum(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1))


# 2.Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.

def calculate_sum_parallel(r_chunks):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, r_chunks)
    return sum(results)


def split_range_chunks(start, end, n_chunks):
    chunk_s = (end - start + 1) // n_chunks
    ranges = [(start + i * chunk_s, start + (i + 1) * chunk_s - 1) for i in range(n_chunks - 1)]
    ranges.append((start + (n_chunks - 1) * chunk_s, end))
    return ranges


# 3. Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
# 4. Print the times it takes for each approach.

if __name__ == "__main__":

    r_chunks = split_range_chunks(1, 2 ** 30, 10)

    start_time = time.time()
    total_sum = calculate_sum_parallel(r_chunks)
    duration_parallel = time.time() - start_time

    print(f"Parallel Sum: {total_sum}")
    print(f"Parallel Duration for multiprocessing: {duration_parallel} sec")
    assert (total_sum == 576460752840294400), "Parallel Sum is not correct."

    start_time = time.time()
    total_sum = calculate_sum(1, 2 ** 30)
    duration = time.time() - start_time

    print(f"Sum: {total_sum}")
    print(f"Duration: {duration} seconds")
    assert total_sum == 576460752840294400, "Sum is not correct."

# Multithreading, IO-bound work (30 points):
# 1. Create a function that sleeps for a random amount of time (<10 seconds),
# prints and returns the sleep duration.


def sleep_func(dummy_argument=None) -> float:
    sleep_duration = random.uniform(0, 10)
    print(f"Sleeping: {sleep_duration:.4f} sec")
    time.sleep(sleep_duration)
    return sleep_duration

# 2. Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# 3. Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time
# (the longest task).
# 4. Print the elapsed time. It should be several times smaller than the "workload" time.


def sleep_parallel() -> None:
    total_workload = 0
    max_workload = 0
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(sleep_func, [None] * 20)
        for duration in results:
            print(f"Sleeping: {duration:.4f} sec")
            total_workload += duration
            if duration > max_workload:
                max_workload = duration

    elapsed_time = time.time() - start_time

    print(f"Total Workload: {total_workload:.4f} sec")
    print(f"Max Workload: {max_workload:.4f} sec")
    print(f"Elapsed Time: {elapsed_time:.4f} sec")


if __name__ == "__main__":
    sleep_parallel()
