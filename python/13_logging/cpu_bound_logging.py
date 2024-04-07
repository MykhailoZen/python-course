import logging
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create file handler and set level to info
file_handler = logging.FileHandler('cpu_bound.log', mode='w')
file_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def calculate_sum(start: int, end: int) -> int:
    """Calculates the sum of numbers in the given range (inclusive)."""
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


def calculate_sum_parallel(start: int, end: int) -> int:
    """Calculates the sum of numbers in the given range (inclusive)
    in parallel."""
    chunk_size = (end - start + 1) // cpu_count()
    chunks = [
        (i, min(i + chunk_size - 1, end))
        for i in range(start, end + 1, chunk_size)
    ]
    with ProcessPoolExecutor() as executor:
        partial_sums = executor.map(
            calculate_sum,
            [chunk_start for chunk_start, _ in chunks],
            [chunk_end for _, chunk_end in chunks],
        )
    return sum(partial_sums)


if __name__ == "__main__":
    target_range = (1, 2**30)
    expected_sum = 576460752840294400

    logger.debug("Starting single process calculation")
    start_time = time.time()
    single_process_sum = calculate_sum(*target_range)
    end_time = time.time()
    single_process_time = end_time - start_time
    logger.debug("Single process calculation completed")

    logger.debug("Starting parallel calculation")
    start_time = time.time()
    parallel_sum = calculate_sum_parallel(*target_range)
    end_time = time.time()
    parallel_time = end_time - start_time
    logger.debug("Parallel calculation completed")

    assert single_process_sum == expected_sum
    assert parallel_sum == expected_sum

    logger.info(f"Single process sum: {single_process_sum}")
    logger.info(f"Single process time: {single_process_time:.4f} seconds")
    logger.info(f"Parallel sum: {parallel_sum}")
    logger.info(f"Parallel time: {parallel_time:.4f} seconds\n\n")
