"""
Multiprocessing, CPU-bound work (30 points):

Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.
Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be the same as for the first function.
Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
Print the times it takes for each approach.
"""

import asyncio
import concurrent.futures
import multiprocessing
import random
import time

"""Create simple calculate_sum function"""


def calculate_sum(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1))


"""Create function to calculate sum in parralel manner with multiprocessing"""


def calculate_sum_parallel(range_chunks):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, range_chunks)
    return sum(results)


"""Create a separate function that takes a chunk and calculates the sum using calculate_sum"""


def calculate_sum_parallel_worker(chunk):
    return calculate_sum(*chunk)


"""Create function to calculate sum in parralel manner with ProcessPoolExecutor"""


def calculate_sum_parallel_future(range_chunks):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(calculate_sum_parallel_worker, range_chunks)
    return sum(results)


"""Splitting the range inti chunks"""


def split_range_into_chunks(start, end, num_chunks):
    chunk_size = (end - start + 1) // num_chunks
    ranges = [
        (start + i * chunk_size, start + (i + 1) * chunk_size - 1)
        for i in range(num_chunks - 1)
    ]
    ranges.append((start + (num_chunks - 1) * chunk_size, end))
    return ranges


if __name__ == "__main__":
    start_range = 1
    end_range = 2 ** 30
    """number of chunks to split the range"""
    num_chunks = 20

    range_chunks = split_range_into_chunks(start_range, end_range, num_chunks)

    start_time = time.time()
    total_sum = calculate_sum_parallel(range_chunks)
    duration_parallel = time.time() - start_time

    print(f"Parallel Sum: {total_sum}")
    print(f"Parallel Duration for multiprocessing: {duration_parallel} seconds")
    assert (
        total_sum == 576460752840294400
    ), "Parallel sum (multiprocessing) is not correct."

    start_time = time.time()
    total_sum_sequential = calculate_sum(start_range, end_range)
    duration_sequential = time.time() - start_time

    print(f"Sequential Sum: {total_sum_sequential}")
    print(f"Sequential Duration: {duration_sequential} seconds")
    assert total_sum_sequential == 576460752840294400, "Sequential sum is not correct."

    start_time = time.time()
    total_sum_concurrent = calculate_sum_parallel_future(range_chunks)
    duration_parallel = time.time() - start_time

    print(f"Parallel Sum: {total_sum_concurrent}")
    print(f"Parallel Duration for concurrent.futures: {duration_parallel} seconds")
    assert (
        total_sum_concurrent == 576460752840294400
    ), "Parallel sum (concurrent.futures) is not correct."


"""
Multithreading, IO-bound work (30 points):
Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
Print the elapsed time. It should be several times smaller than the "workload" time.
"""


def random_sleep(dummy_argument=None) -> float:
    sleep_duration = random.uniform(
        0, 10
    )  # Generate a random sleep duration between 0 and 10 seconds
    print(f"Sleeping for {sleep_duration:.2f} seconds")
    time.sleep(sleep_duration)  # Sleep for the generated duration
    return sleep_duration


def call_random_sleep_parallel() -> None:
    total_workload_time = 0
    max_workload_time = 0
    start_time = time.time()  # Record the start time

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(
            random_sleep, [None] * 20
        )  # Pass a list of 20 None values as the argument
        for duration in results:
            print(f"Slept for {duration:.2f} seconds.")
            total_workload_time += duration
            if duration > max_workload_time:
                max_workload_time = duration

    elapsed_time = time.time() - start_time  # Calculate elapsed time

    print(f"Total Workload Time: {total_workload_time:.2f} seconds")
    print(f"Max Workload Time: {max_workload_time:.2f} seconds")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")  # Print elapsed time


# Example usage
if __name__ == "__main__":
    call_random_sleep_parallel()


"""
(optional) asyncio practice: Implement the multithreading task above using the asyncio approach.
"""


async def random_sleep() -> float:
    sleep_duration = random.uniform(
        0, 10
    )  # Generate a random sleep duration between 0 and 10 seconds
    print(f"Sleeping for {sleep_duration:.2f} seconds")
    await asyncio.sleep(sleep_duration)  # Sleep for the generated duration
    return sleep_duration


async def call_random_sleep_parallel() -> None:
    total_workload_time = 0
    max_workload_time = 0

    start_time = time.time()  # Record the start time

    tasks = [random_sleep() for _ in range(20)]
    results = await asyncio.gather(*tasks)

    for duration in results:
        print(f"Slept for {duration:.2f} seconds.")
        total_workload_time += duration
        if duration > max_workload_time:
            max_workload_time = duration

    elapsed_time = time.time() - start_time  # Calculate elapsed time

    print(f"Total Workload Time: {total_workload_time:.2f} seconds")
    print(f"Max Workload Time: {max_workload_time:.2f} seconds")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")  # Print elapsed time


# Example usage
if __name__ == "__main__":
    asyncio.run(call_random_sleep_parallel())
