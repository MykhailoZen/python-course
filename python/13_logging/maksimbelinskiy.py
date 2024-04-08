import concurrent.futures
import logging
import multiprocessing
import random
import time

log = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
log.setLevel(level=logging.DEBUG)


log_stream = logging.StreamHandler()
log_stream.setLevel(level=logging.DEBUG)
log_stream.setFormatter(formatter)
log.addHandler(log_stream)

log_file = logging.FileHandler("concurrency.log", mode="w")
log_file.setLevel(level=logging.INFO)
log_file.setFormatter(formatter)
log.addHandler(log_file)


def calculate_sum(start: int, end: int) -> int:
    """
    Calculate the sum of numbers in the given range including both ends.

    Parameters:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        int: The sum of numbers in the range.
    """
    return sum(range(start, end + 1))


def chunk_sum(chunk):
    """
    Calculate the sum of numbers in a given chunk.

    Parameters:
        chunk (tuple): A tuple containing the start and end of the chunk.

    Returns:
        int: The sum of numbers in the chunk.
    """
    start, end = chunk
    return calculate_sum(start, end)


def calculate_sum_parallel(
    start: int, end: int, chunk_size: int = 10_000_000
) -> int:  # noqa: E501
    """
    Calculate the sum of numbers in the given range in parallel.

    Parameters:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        chunk_size (int): The size of each chunk.

    Returns:
        int: The total sum of numbers in the range.
    """
    total_sum = 0
    with multiprocessing.Pool() as pool:
        chunks = [
            (i, min(i + chunk_size - 1, end))
            for i in range(start, end + 1, chunk_size)  # noqa: E501
        ]
        chunk_sums = pool.map(chunk_sum, chunks)
        total_sum = sum(chunk_sums)
    return total_sum


if __name__ == "__main__":
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    end_time = time.time()
    log.info("Parallel calculation result: %s", result_parallel)
    log.info("Time taken for parallel calculation: %s", end_time - start_time)

    start_time = time.time()
    result_parallel = calculate_sum(1, 2**30)
    end_time = time.time()
    log.info("Calculation result: %s", result_parallel)
    log.info("Time taken for calculation: %s", end_time - start_time)


def sleep_and_print() -> float:
    """
    Sleep for a random amount of time (<10 seconds), print the sleep duration,
    and return the sleep duration.

    Returns:
        float: The sleep duration.
    """
    sleep_duration = random.uniform(0, 10)
    log.debug("Sleeping for %s seconds...", sleep_duration)
    time.sleep(sleep_duration)
    log.debug("Finished sleeping.")
    return sleep_duration


def call_sleep_function_parallel():
    """
    Call the sleep_and_print function 20 times using multiple threads in parallel.
    Calculate total workload time, max workload time, and elapsed time.
    """  # noqa: E501
    start_time = time.time()
    total_workload = 0
    max_workload = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_and_print) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            total_workload += result
            if result > max_workload:
                max_workload = result

    elapsed_time = time.time() - start_time

    return total_workload, max_workload, elapsed_time


if __name__ == "__main__":
    total_workload, max_workload, elapsed_time = call_sleep_function_parallel()
    log.info("Total workload time: %s", total_workload)
    log.info("Max workload time: %s", max_workload)
    log.info("Elapsed time: %s", elapsed_time)
