import concurrent.futures
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('info.log')
file_handler.setLevel(logging.INFO)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

"""Multiprocessing, CPU-bound work (30 points):

Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given 
range including both ends. Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a 
parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given 
range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be 
the same as for the first function. Run both functions for the range [1, 2**30], verify the result is 
576460752840294400. Print the times it takes for each approach."""


def calculate_sum(start: int, end: int):
    return sum(range(start, end + 1))


def calculate_sum_parallel(start: int, end: int, num_processes: int):
    chunk_size = (end - start + 1) // num_processes
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(calculate_sum, i, min(i + chunk_size, end + 1)) for i in
                   range(start, end + 1, chunk_size)]
        results = [future.result() for future in futures]
    return sum(results)


if __name__ == '__main__':
    start_time = time.time()
    sequential_result = calculate_sum(1, 2 ** 30)
    logging.debug(f"Sequential Result:{sequential_result}")
    duration_sequential = time.time() - start_time
    logger.info(f"Sequential Duration: {duration_sequential:.2f} seconds")

    start_time = time.time()
    parallel_result = calculate_sum_parallel(1, 2 ** 30, 10)
    logging.debug(f"Parallel Result:{parallel_result}")
    duration_parallel = time.time() - start_time
    logger.info(f"Parallel Duration: {duration_parallel:.2f} seconds")
