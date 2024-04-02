#2. Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
# Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.



import random
import time
import concurrent.futures


def sleep_random_time():
    sleep_time = random.uniform(0, 10)
    time.sleep(sleep_time)
    print(f"System is slept {sleep_time} sec")
    return sleep_time


def parallel_sleeps():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Schedule the sleep_random_time function 20 times in parallel using a lambda function
        results = list(executor.map(lambda _: sleep_random_time(), range(20)))

    workload_time_toral = sum(results)
    workload_time_max = max(results)

    print(f"Total workload time: {workload_time_toral} sec")
    print(f"Max workload time: {workload_time_max} sec")


if __name__ == "__main__":
    start = time.time()
    parallel_sleeps()
    elapsed_time = time.time() - start
    print(f"Elapsed time: {elapsed_time} seconds")


# 1.
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.
# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be the same as for the first function.
# Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
# Print the times it takes for each approach.

import multiprocessing
import time

def sum_calc(start: int, end: int) -> int:
    return sum(range(start, end + 1))

def sum_parallel(start: int, end: int, chunk_size: int) -> int:
    chunks = [(i, min(i + chunk_size, end)) for i in range(start, end + 1, chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.starmap(sum_calc, chunks)

    total_sum = sum(results)
    return total_sum

if __name__ == "__main__":
    start = time.time()
    serial_result = sum_calc(1, 2 ** 30)
    serial_time = time.time() - start

    start = time.time()
    parallel_result = sum_parallel(1, 2 ** 30, chunk_size=10 ** 7)
    parallel_time = time.time() - start

    print(f"Serial sum is {serial_result}. Time: {serial_time} sec")
    print(f"Parallel sum is {parallel_result}. Time: {parallel_time} sec")
    print(f"Difference between Serial and Parallel times is {serial_time - parallel_time} sec")

# Verify the result is 576460752840294400 of both function.

    def check_serial():
        if serial_result == 576460752840294400:
            print("Yes, serial result is correct.")
        else:
            print(f"No, serial result is unexpected. Actual result is {serial_result}.")

    def check_paralel():
        if parallel_result == 576460752840294400:
            print("Yes, parallel result is correct.")
        else:
            print(f"No, parallel result is unexpected. Actual result is {parallel_result}.")

    check_serial()
    check_paralel()