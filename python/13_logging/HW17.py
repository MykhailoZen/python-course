import asyncio
import concurrent.futures
import logging
import multiprocessing
import os
import random
import threading
import time

# Get the current directory
current_directory = os.path.dirname(os.path.realpath(__file__))
log_file_path = os.path.join(current_directory, "info.log")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a file handler for INFO+ messages
info_file_handler = logging.FileHandler(log_file_path)
info_file_handler.setLevel(logging.INFO)
info_file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
logging.getLogger("").addHandler(info_file_handler)

# Multiprocessing, CPU-bound work:


def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


def calculate_sum_partial(args):
    return calculate_sum(*args)


def calculate_sum_parallel(start: int, end: int) -> int:
    chunk_size = (end - start + 1) // multiprocessing.cpu_count()
    ranges = [(i, min(i + chunk_size - 1, end)) for i in range(start, end, chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sum_partial, ranges)

    return sum(results)


class Calculator:
    def __init__(self):
        pass


if __name__ == "__main__":
    calculator = Calculator()

    logging.info("Starting serial calculation")
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time
    logging.info("Serial calculation completed")

    logging.info("Starting parallel calculation")
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    parallel_time = time.time() - start_time
    logging.info("Parallel calculation completed")

    logging.info("Serial Result: %d", result_serial)
    logging.info("Parallel Result: %d", result_parallel)
    logging.info("Serial Time: %.2f", serial_time)
    logging.info("Parallel Time: %.2f", parallel_time)


# Multithreading, IO-bound work:


def random_sleep() -> float:
    sleep_duration = random.random() * 10
    time.sleep(sleep_duration)
    thread_name = threading.current_thread().name
    logging.debug(f"Thread {thread_name} slept for {sleep_duration:.2f} seconds")
    return sleep_duration


def run_parallel_tasks():
    logging.info("Starting parallel tasks")
    start_time = time.time()
    total_workload = 0
    max_workload = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]

        for future in concurrent.futures.as_completed(futures):
            sleep_duration = future.result()
            total_workload += sleep_duration
            if sleep_duration > max_workload:
                max_workload = sleep_duration

    elapsed_time = time.time() - start_time

    logging.info("Parallel tasks completed")
    logging.info("Total Workload Time: %.2f", total_workload)
    logging.info("Max Workload Time: %.2f", max_workload)
    logging.info("Elapsed Time: %.2f", elapsed_time)


class TaskManager:
    def __init__(self):
        pass


if __name__ == "__main__":
    task_manager = TaskManager()
    run_parallel_tasks()


# (optional) asyncio practice:


async def random_sleep() -> float:
    sleep_duration = random.random() * 10
    await asyncio.sleep(sleep_duration)
    logging.debug(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration


async def run_parallel_tasks():
    logging.info("Starting asyncio tasks")
    start_time = time.time()
    total_workload = 0
    max_workload = 0

    tasks = [random_sleep() for _ in range(20)]
    completed_tasks = await asyncio.gather(*tasks)

    for sleep_duration in completed_tasks:
        total_workload += sleep_duration
        if sleep_duration > max_workload:
            max_workload = sleep_duration

    elapsed_time = time.time() - start_time

    logging.info("Asyncio tasks completed")
    logging.info("Total Workload Time: %.2f", total_workload)
    logging.info("Max Workload Time: %.2f", max_workload)
    logging.info("Elapsed Time: %.2f", elapsed_time)


class TaskManagerAsync:
    def __init__(self):
        pass


if __name__ == "__main__":
    task_manager_async = TaskManagerAsync()
    asyncio.run(run_parallel_tasks())
