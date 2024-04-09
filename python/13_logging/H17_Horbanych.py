import logging
import multiprocessing
import concurrent.futures
import random
import time

# Add logging to the code implemented in the "Concurrency" module.
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

def calculate_sum_parallel(range_chunks):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, range_chunks)
    return sum(results)

def calculate_sum_parallel_worker(chunk):
    return calculate_sum(*chunk)

def calculate_sum_parallel_future(range_chunks):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(calculate_sum_parallel_worker, range_chunks)
    return sum(results)

def split_range_into_chunks(start, end, num_chunks):
    chunk_size = (end - start + 1) // num_chunks
    ranges = [(start + i*chunk_size, start + (i+1)*chunk_size - 1) for i in range(num_chunks - 1)]
    ranges.append((start + (num_chunks - 1)*chunk_size, end))
    return ranges

if __name__ == "__main__":
    start_range = 1
    end_range = 2 ** 30
    num_chunks = 20

    range_chunks = split_range_into_chunks(start_range, end_range, num_chunks)

    logging.info("Starting CPU-bound work...")

    start_time = time.time()
    total_sum = calculate_sum_parallel(range_chunks)
    duration_parallel = time.time() - start_time

    logging.info("Parallel Sum: %s", total_sum)
    logging.info("Parallel Duration for multiprocessing: %s seconds", duration_parallel)

    start_time = time.time()
    total_sum_sequential = calculate_sum(start_range, end_range)
    duration_sequential = time.time() - start_time

    logging.info("Sequential Sum: %s", total_sum_sequential)
    logging.info("Sequential Duration: %s seconds", duration_sequential)

    start_time = time.time()
    total_sum = calculate_sum_parallel_future(range_chunks)
    duration_parallel = time.time() - start_time

    logging.info("Parallel Sum: %s", total_sum)
    logging.info("Parallel Duration for concurrent.futures: %s seconds", duration_parallel)


# Multithreading, IO-bound work
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

def random_sleep(dummy_argument=None) -> float:
    sleep_duration = random.uniform(0, 10)
    logging.info("Sleeping for %.2f seconds", sleep_duration)
    time.sleep(sleep_duration)
    return sleep_duration

def call_random_sleep_parallel() -> None:
    total_workload_time = 0
    max_workload_time = 0
    logging.info("Starting IO-bound work...")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(random_sleep, [None] * 20)
        for duration in results:
            logging.info("Slept for %.2f seconds.", duration)
            total_workload_time += duration
            if duration > max_workload_time:
                max_workload_time = duration

    elapsed_time = time.time() - start_time

    logging.info("Total Workload Time: %.2f seconds", total_workload_time)
    logging.info("Max Workload Time: %.2f seconds", max_workload_time)
    logging.info("Elapsed Time: %.2f seconds", elapsed_time)

# For run
if __name__ == "__main__":
    call_random_sleep_parallel()
