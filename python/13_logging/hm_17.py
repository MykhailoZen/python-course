import concurrent.futures
import logging
import random
import time

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)

log_stream = logging.StreamHandler()
log_file = logging.FileHandler(filename='log_info.txt', mode='a')
log_file.setLevel(level=logging.INFO)
log_stream.setLevel(level=logging.DEBUG)
log_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_stream.setFormatter(log_file_formatter)
log_file.setFormatter(log_file_formatter)
log.addHandler(log_stream)
log.addHandler(log_file)


def calculate_sum(start: int, end: int) -> int:
    result = sum(i for i in range(start, end + 1))
    return result


def calculate_sum_parallel(start: int, end: int, chunk_size: int = 1000000) -> int:
    log.debug(
        f"Start calculate_sum_parallel with params: start = {start}, end = {end}, chunk_size: {chunk_size}"  # noqa: LOG011
    )
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(calculate_sum, chunk_start, chunk_end) for chunk_start, chunk_end in chunks]
        results = [future.result() for future in futures]
    return sum(results)


def sleep_random():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    log.debug(f"Sleep duration = {sleep_duration}")
    return sleep_duration


def run_sleep_random():
    start_time = time.time()
    total_workload_time = 0
    max_workload_time = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_random) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            total_workload_time += result
            max_workload_time = max(max_workload_time, result)

    elapsed_time = time.time() - start_time

    log.info(f"Total workload time: {total_workload_time:.2f} seconds")  # noqa: LOG011
    log.info(f"Max workload time: {max_workload_time:.2f} seconds")  # noqa: LOG011
    log.info(f"Elapsed time: {elapsed_time:.2f} seconds")  # noqa: LOG011
    return max_workload_time, total_workload_time, elapsed_time


if __name__ == "__main__":
    # Verification run calculate_sum()
    start = 1
    end = 2**30

    start_time = time.time()
    log.debug("Call calculate_sum")
    log.debug(f"Start calculation of calculate_sum with parameters: start = {start}, end = {end}")  # noqa: LOG011
    result = calculate_sum(start, end)
    time_result = time.time() - start
    log.info(f"Time spend calculate_sum: {time_result}")
    log.info(f"Returns the sum of numbers from {start} to {end} = {result}")  # noqa: LOG011
    log.debug("Calculate_sum completed")

    # Verification run calculate_sum_parallel()
    start_time = time.time()
    log.debug("Call calculate_sum_paralle")
    sum_result = calculate_sum_parallel(start, end)
    time_result = time.time() - start_time
    log.info(f"Time spend calculate_sum_parallel: {time_result}")
    log.info(f"Returns the sum of numbers in a parallel manner from {start} to {end} = {sum_result}")  # noqa: LOG011
    log.debug("Calculate_sum_paralle completed")

    # Verification run sleep_random()
    log.debug("Call sleep_random")
    result_sleep = sleep_random()
    log.info(f"Result of sleep_random = {result_sleep}")
    log.debug("Sleep_random completed")

    # Verification run run_sleep_random()
    log.debug("Call run_sleep_random")
    run_sleep_random()
    log.debug("Run_sleep_random completed")
