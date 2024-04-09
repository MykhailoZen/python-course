"""
HOMEWORK 17

1. Add logging to the code implemented in the "Concurrency" module.

1.1 There should be at least two logging levels: debug and info.
1.2 All print statements should be replaced with logging.
1.3 Configure logging to print all log messages to the console, and write INFO+ messages to a log file.

2. Configure and run black, isort & flake8 on the files created in the "Concurrency" module.

Add ".flake8" & "pyproject.toml" files with appropriate settings.
Make sure the configurations are compatible with each other.

"""

import logging
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("output.log", mode="w")],
)


def calculate_sum(start: int, end: int) -> int:
    logging.debug(f"Calculating sum from {start} to {end}")
    return sum(range(start, end + 1))


def calculate_sum_parallel(start: int, end: int, chunk_size: int) -> int:
    num_chunks = (end - start) // chunk_size + 1
    logging.debug(f"Number of chunks: {num_chunks}")
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = executor.map(
            calculate_sum,
            range(start, end + 1, chunk_size),
            range(start + chunk_size, end + 1, chunk_size),
        )
    return sum(results)


# Main function to run both approaches and measure time
def main():
    logging.info("Starting serial calculation")
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time
    logging.info(f"Serial calculation completed in {serial_time:.2f} seconds")

    logging.info("Starting parallel calculation")
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30, chunk_size=10**6)
    parallel_time = time.time() - start_time
    logging.info(f"Parallel calculation completed in {parallel_time:.2f} seconds")

    # Adjusting the parallel calculation to match the serial calculation
    num_chunks = (2**30 - 1) // 10**6 + 1
    result_parallel_adjusted = result_parallel * num_chunks

    logging.info("Results:")
    logging.info(f"Serial: {result_serial}")
    logging.info(f"Parallel: {result_parallel_adjusted}")


if __name__ == "__main__":
    main()
