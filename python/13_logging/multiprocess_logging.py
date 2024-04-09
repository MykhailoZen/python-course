import time
import logging
from multiprocessing import Pool, cpu_count
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("multiprocess.txt", mode="a")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def measure_time(func):
    """Measure the time taken by a function to execute"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_to_return = func(*args, **kwargs)
        end_time = time.time()
        time_for_execution = end_time - start_time
        logger.info(
            f"Time spent for function {func.__name__}:\n"
            f"{time_for_execution:.4f} seconds"
        )
        return function_to_return

    return wrapper


@measure_time
def calculate_sum(start, end):
    """Calculate the sum of the given range of numbers"""
    logger.debug("Started executing calculate_sum function")
    result = 0
    for number in range(start, end + 1):
        result += number
    logger.debug(f"calculate_sum execution finished, " f"returning {result}")
    return result


@measure_time
def calculate_multiple_cpu(start, end):
    """Execute another function in parallel on the specified number of CPUs"""
    logger.debug("Started executing calculate_multiple_cpu function")
    total_numbers = end - start + 1
    chunk_size = total_numbers // cpu_count()
    remainder = total_numbers % cpu_count()
    ranges = []
    current_start = start
    for i in range(cpu_count()):
        chunk_end = current_start + chunk_size - 1
        if i < remainder:
            chunk_end += 1
        ranges.append((current_start, chunk_end))
        logger.debug(f"Adding chunk: {current_start}, " f"{chunk_end}")
        current_start = chunk_end + 1
    logger.debug(f"Range for calculation: {ranges}")
    with Pool(processes=cpu_count()) as pool:
        results = pool.starmap(calculate_sum, ranges)
    logger.debug("calculate_multiple_cpu calculating sum...")
    return sum(results)


if __name__ == "__main__":
    start_range = 1
    end_range = 2**30
    logger.info(calculate_sum(start_range, end_range))
    logger.info(calculate_multiple_cpu(start_range, end_range))
