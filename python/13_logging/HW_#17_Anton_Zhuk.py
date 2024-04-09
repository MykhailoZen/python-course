import concurrent.futures
import logging.config
import multiprocessing
import random
import time

logging.config.fileConfig(
    fname="config.ini",
    disable_existing_loggers=False,
)
logger = logging.getLogger(__name__)

# Multiprocessing, CPU-bound work (30 points):
# 1. Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
# 2. Create another function (e.g. "calculate_sum_parallel") that calls
# "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or
# "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks,
# obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.
# 3. Run both functions for the range [1, 2**30],
# verify the result is 576460752840294400.
# 4. Print the times it takes for each approach.


def calculate_sum(start: int, end: int) -> int:
    total = 0
    logger.debug(f"Starting calculation: start: {start}, end: {end}")
    for i in range(start, end + 1):
        total += i
    logger.debug(f"Compete calculation: start: {start}, end: {end}")
    logger.info(f"Total calculation: {total}")
    return total


def calculate_sum_parallel(
    start: int, end: int, chunk_size: int = 10000
) -> int:
    chunks = [
        (i, min(i + chunk_size - 1, end))
        for i in range(start, end + 1, chunk_size)
    ]
    logger.debug(f"Chunks: {chunks}")
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.starmap(calculate_sum, chunks)
    sum_result = sum(result)
    logger.info(f"Calculated sum: {sum_result}")
    return sum_result


# Multithreading, IO-bound work (30 points):
# 1. Create a function that sleeps for a random amount of time (<10 seconds),
# prints and returns the sleep duration.
# 2. Create another function that calls the previous one 20 times using
# multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# 3. Print the "total workload" time (the sum of outputs from all calls) and
# the "max workload" time (the longest task).
# 4. Print the elapsed time. It should be several times smaller than
# the "workload" time.
def sleep():
    sleep_time = random.uniform(1, 10)
    logger.debug(f"Started sleep: {sleep_time}")
    time.sleep(sleep_time)
    logger.debug(f"Finished sleep: {sleep_time}")
    return sleep_time


def tasks_parallel():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep) for _ in range(20)]
        results = [
            future.result()
            for future in concurrent.futures.as_completed(futures)
        ]

    total_workload_time = sum(results)
    max_workload_time = max(results)
    logger.info(f"Total Workload Time: {total_workload_time} sec")
    logger.info(f"Max Workload Time: {max_workload_time} sec")

    return total_workload_time, max_workload_time


if __name__ == "__main__":
    expected_result = 576460752840294400

    start_time = time.time()
    result_sequential = calculate_sum(1, 2**30)
    sequential_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    parallel_time = time.time() - start_time

    logger.info(f"Sequentially Sum: {result_sequential}")
    logger.info(f"Sequentially Time : {sequential_time} sec")
    logger.info(f"Parallel Sum : {result_parallel}")
    logger.info(f"Parallel Time: {parallel_time} sec")

    if result_sequential == result_parallel == expected_result:
        logging.info("Results the same.")
    else:
        logging.info("Results mismatch.")

    start_time = time.time()
    total_workload_time, max_workload_time = tasks_parallel()
    elapsed_time = time.time() - start_time

    logger.info(f"Elapsed Time: {elapsed_time} sec")
