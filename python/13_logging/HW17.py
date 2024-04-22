import logging
import random

import concurrent.futures
import multiprocessing
import time

# 1.Add logging to the code implemented in the "Concurrency" module.
# There should be at least two logging levels: debug and info.
# All print statements should be replaced with logging.
# Configure logging to print all log messages to the console, and write INFO+ messages to a log file.

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S:%mS",
)

logger = logging.getLogger(__name__)

handler = logging.FileHandler("test.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


def calculate_sum(start: int, end: int) -> int:
    return sum(i for i in range(start, end + 1))


def calculate_sum_parallel(r_chunks):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, r_chunks)
    return sum(results)


def split_range_chunks(start, end, n_chunks):
    chunk_s = (end - start + 1) // n_chunks
    ranges = [
        (start + i * chunk_s, start + (i + 1) * chunk_s - 1) for i in range(n_chunks - 1)
    ]
    ranges.append((start + (n_chunks - 1) * chunk_s, end))
    return ranges


if __name__ == "__main__":

    r_chunks = split_range_chunks(1, 2**30, 10)

    start_time = time.time()
    total_sum = calculate_sum_parallel(r_chunks)
    duration_parallel = time.time() - start_time

    logger.info(f"Parallel Sum: {total_sum}")
    logger.info(f"Parallel Duration for multiprocessing: {duration_parallel} sec")
    assert total_sum == 576460752840294400, "Parallel Sum is not correct."

    start_time = time.time()
    total_sum = calculate_sum(1, 2**30)
    duration = time.time() - start_time

    logger.info(f"Sum: {total_sum}")
    logger.info(f"Duration: {duration} seconds")
    assert total_sum == 576460752840294400, "Sum is not correct."


def sleep_func(dummy_argument=None) -> float:
    sleep_duration = random.uniform(0, 10)
    logger.info(f"Sleeping: {sleep_duration:.4f} sec")
    time.sleep(sleep_duration)
    return sleep_duration


def sleep_parallel() -> None:
    total_workload = 0
    max_workload = 0
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(sleep_func, [None] * 20)
        for duration in results:
            logger.info(f"Sleeping: {duration:.4f} sec")
            total_workload += duration
            if duration > max_workload:
                max_workload = duration

    elapsed_time = time.time() - start_time

    logger.info(f"Total Workload: {total_workload:.4f} sec")
    logger.info(f"Max Workload: {max_workload:.4f} sec")
    logger.info(f"Elapsed Time: {elapsed_time:.4f} sec")


if __name__ == "__main__":
    sleep_parallel()
