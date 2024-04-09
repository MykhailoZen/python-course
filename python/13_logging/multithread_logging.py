import time
from concurrent.futures import ThreadPoolExecutor
import random
import logging


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("multithread.txt", mode="w")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def execute_random_sleep_with_threads(num_tasks):
    """Execute random_sleep function multiple times using ThreadPoolExecutor"""
    result_list = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(random_sleep) for task in range(num_tasks)]
        for future in futures:
            result_list.append(future.result())
    logger.debug(f"execute_random_sleep_with_threads returning {result_list}")
    return result_list


def random_sleep() -> float:
    """Generate a random value, sleep for that time, and return time spent"""
    function_start_time = time.time()
    seconds_to_sleep = random.randint(1, 9)
    time.sleep(seconds_to_sleep)
    function_end_time = time.time()
    function_exec_time = function_end_time - function_start_time
    logger.debug(f"function random_sleep returning {function_exec_time}")
    return float("{:.1f}".format(function_exec_time))


if __name__ == "__main__":
    logger.debug("Started execution of the program")
    execute_times = 20
    start_time = time.time()
    result = execute_random_sleep_with_threads(execute_times)
    end_time = time.time()
    time_spent = end_time - start_time
    total_workload = sum(result)
    max_workload = max(result)
    logger.info(f"Sum of outputs from all calls: {total_workload} sec")
    logger.info(f"The longest task: {max_workload} sec")
    logger.info(f"Elapsed time: {time_spent:.2f} sec")
    logger.debug("Program execution finished")
