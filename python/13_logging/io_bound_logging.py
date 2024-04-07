import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create file handler and set level to info
file_handler = logging.FileHandler('io_bound.log', mode='w')
file_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def io_bound_task():
    """Simulates an IO-bound task by sleeping for a random amount of time
    (up to 10 seconds)."""
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    logger.debug(f"Task slept for {sleep_duration:.2f} seconds.")
    return sleep_duration


def run_parallel_tasks():
    """Runs multiple IO-bound tasks in parallel using ThreadPoolExecutor."""
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(io_bound_task) for _ in range(20)]

    workload_times = [result.result() for result in results]
    total_workload = sum(workload_times)
    max_workload = max(workload_times)

    logger.info(f"Total workload time: {total_workload:.2f} seconds.")
    logger.info(f"Max workload time: {max_workload:.2f} seconds.")

    return workload_times


if __name__ == "__main__":
    start_time = time.time()
    workload_times = run_parallel_tasks()
    elapsed_time = time.time() - start_time

    logger.info(f"Elapsed time: {elapsed_time:.2f} seconds.")
