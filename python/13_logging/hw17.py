"""Modules for tasks"""
import concurrent.futures
import logging
import multiprocessing
import random
import time

# create a config logger for printing all info DEBUG+ for debugging in console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s -- %(levelname)s -- %(message)s",
    handlers=[logging.StreamHandler(),],
)
logger = logging.getLogger(__name__)

# created and configurate new handler for writing INFO+ to file
file_handler = logging.FileHandler("test17.log")
file_handler.setLevel(logging.INFO)
file_handler_format = logging.Formatter(
    "%(asctime)s -- %(levelname)s -- %(message)s"
)
file_handler.setFormatter(file_handler_format)
logger.addHandler(file_handler)


# 2.TASK from hw15 """Function for generate a random time"""
def sleep_random_time():
    sleep_time = random.uniform(0, 10)
    time.sleep(sleep_time)
    logger.debug(f"System is slept {sleep_time} sec")
    return sleep_time


"""Function for executing task in parrallel"""


def parallel_sleeps():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Schedule the sleep_random_time function 20 times in parallel using
        # a lambda function
        results = list(executor.map(lambda _: sleep_random_time(), range(20)))

    workload_time_toral = sum(results)
    workload_time_max = max(results)

    logger.info(f"Total workload time: {workload_time_toral} sec")
    logger.info(f"Max workload time: {workload_time_max} sec")


if __name__ == "__main__":
    start = time.time()
    parallel_sleeps()
    elapsed_time = time.time() - start
    logger.info(f"Elapsed time: {elapsed_time} seconds")


# 1. TASK from hw15


"""Function sum calc"""


def sum_calc(start: int, end: int) -> int:
    return sum(range(start, end + 1))


"""Function sum calc in parallel"""


def sum_parallel(start: int, end: int, chunk_size: int) -> int:
    chunks = [(i, min(i + chunk_size, end))
              for i in range(start, end + 1, chunk_size)
              ]
    with multiprocessing.Pool() as pool:
        results = pool.starmap(sum_calc, chunks)
    total_sum = sum(results)
    return total_sum


if __name__ == "__main__":
    start = time.time()
    serial_result = sum_calc(1, 2**30)
    serial_time = time.time() - start

    start = time.time()
    parallel_result = sum_parallel(1, 2**30, chunk_size=10**7)
    parallel_time = time.time() - start

    logger.info(f"Serial sum is {serial_result}. Time: {serial_time} sec")
    logger.info(f"Parallel sum is {parallel_result}. "
                f"Time: {parallel_time} sec"
                )
    logger.debug(
        f"Difference between Serial and Parallel times is"
        f" {serial_time - parallel_time} sec"
    )
