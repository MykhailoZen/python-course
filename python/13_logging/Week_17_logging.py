import logging
import random

import asyncio
import concurrent.futures
import multiprocessing
import time

# Configure logging to print all log messages to the console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S:%mS",
)

# Create a logger
logger = logging.getLogger(__name__)

# Create a handler for writing INFO+ messages to a log file
file_handler = logging.FileHandler("multiprocessing.log")
file_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

"""Create simple calculate_sum function"""


def calculate_sum(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1))


"""Create function to calculate sum in parallel manner with multiprocessing"""


def calculate_sum_parallel(range_chunks):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, range_chunks)
    return sum(results)


"""Create a separate function that takes a chunk and calculates the sum using calculate_sum"""


def calculate_sum_parallel_worker(chunk):
    return calculate_sum(*chunk)


"""Create function to calculate sum in parallel manner with ProcessPoolExecutor"""


def calculate_sum_parallel_future(range_chunks):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(calculate_sum_parallel_worker, range_chunks)
    return sum(results)


"""Splitting the range into chunks"""


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

    logger.info(f"Parallel Sum: {total_sum}")
    logger.info(f"Parallel Duration for multiprocessing: {duration_parallel} seconds")
    assert (
        total_sum == 576460752840294400
    ), f"Parallel sum (multiprocessing) is not correct. Expected: 576460752840294400, Actual: {total_sum}"

    start_time = time.time()
    total_sum_sequential = calculate_sum(start_range, end_range)
    duration_sequential = time.time() - start_time

    logger.info(f"Sequential Sum: {total_sum_sequential}")
    logger.info(f"Sequential Duration: {duration_sequential} seconds")
    assert (
        total_sum_sequential == 576460752840294400
    ), f"Sequential sum is not correct. Expected: 576460752840294400, Actual: {total_sum_sequential}"

    start_time = time.time()
    total_sum_concurrent = calculate_sum_parallel_future(range_chunks)
    duration_parallel = time.time() - start_time

    logger.info(f"Parallel Sum: {total_sum_concurrent}")
    logger.info(
        f"Parallel Duration for concurrent.futures: {duration_parallel} seconds"
    )
    assert (
        total_sum_concurrent == 576460752840294400
    ), f"Parallel sum (concurrent.futures) is not correct. Expected: 576460752840294400, Actual: {total_sum_concurrent}"


"""
Multithreading, IO-bound work (30 points):
Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
Create another function that calls the previous one 20 times using multiple threads in parallel 
(e.g. use "concurrent.futures.ThreadPoolExecutor" class).
Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
Print the elapsed time. It should be several times smaller than the "workload" time.
"""


def random_sleep(dummy_argument=None) -> float:
    sleep_duration = random.uniform(0, 10)
    logger.info(f"Sleeping for {sleep_duration:.2f} seconds")
    time.sleep(sleep_duration)
    return sleep_duration


def call_random_sleep_parallel() -> None:
    total_workload_time = 0
    max_workload_time = 0
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(random_sleep, [None] * 20)
        for duration in results:
            logger.info(f"Slept for {duration:.2f} seconds.")
            total_workload_time += duration
            if duration > max_workload_time:
                max_workload_time = duration

    elapsed_time = time.time() - start_time

    logger.info(f"Total Workload Time: {total_workload_time:.2f} seconds")
    logger.info(f"Max Workload Time: {max_workload_time:.2f} seconds")
    logger.info(f"Elapsed Time: {elapsed_time:.2f} seconds")


# Example usage
if __name__ == "__main__":
    call_random_sleep_parallel()


"""
(optional) asyncio practice: Implement the multithreading task above using the asyncio approach.
"""


async def random_sleep() -> float:
    sleep_duration = random.uniform(0, 10)
    logger.info(f"Sleeping for {sleep_duration:.2f} seconds")
    await asyncio.sleep(sleep_duration)
    return sleep_duration


async def call_random_sleep_parallel() -> None:
    total_workload_time = 0
    max_workload_time = 0
    start_time = time.time()

    tasks = [random_sleep() for _ in range(20)]
    results = await asyncio.gather(*tasks)

    for duration in results:
        logger.info(f"Slept for {duration:.2f} seconds.")
        total_workload_time += duration
        if duration > max_workload_time:
            max_workload_time = duration

    elapsed_time = time.time() - start_time

    logger.info(f"Total Workload Time: {total_workload_time:.2f} seconds")
    logger.info(f"Max Workload Time: {max_workload_time:.2f} seconds")
    logger.info(f"Elapsed Time: {elapsed_time:.2f} seconds")


# Example usage
if __name__ == "__main__":
    asyncio.run(call_random_sleep_parallel())
