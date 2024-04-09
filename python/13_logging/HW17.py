import random
import time
import multiprocessing
import concurrent.futures
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(processName)s: %(message)s')

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(processName)5s- %(message)s')
log_handler = logging.FileHandler("HW16-logs.txt")
log_handler.setLevel(logging.INFO)
log_handler.setFormatter(log_format)
logging.getLogger().addHandler(log_handler)

# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
def calculate_sum(start: int, end: int) -> int:
    """
    :param start: start of range
    :param end: end of range
    :return: sum of range
    """
    res = 0
    for i in range(start, end+1):
        res += i
    logging.debug(f'Total sum is {res}')
    return res


# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.
def calculate_sum_parallel(start: int, end: int) -> int:
    """
    :param start: start of range
    :param end: end of range
    :return: sum of range
    """
    num_chunks = multiprocessing.cpu_count()
    chunk_size = (end - start + 1) // num_chunks
    logging.debug(f'Amount of CPUs - {num_chunks}, chunk size is {chunk_size}')
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    logging.debug(f'Amount of chunks - {chunks}')

    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, chunks)

    return sum(results)


# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
def sleep_randomiser():
    sleep_dur = random.random() * 10
    logging.info(f'Duration of sleep - {sleep_dur}')
    time.sleep(sleep_dur)
    logging.debug(f'Sleeping for {sleep_dur}')
    return sleep_dur


# Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.
def sleep_parallel():
    workload_total = 0
    workload_max = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_randomiser) for _ in range(20)]

        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            workload_total += result
            workload_max = max(workload_max, result)

    return workload_total, workload_max


def main():

    logging.debug(f'Timer successfully started')
    time_start = time.perf_counter()
    func_1 = calculate_sum(1, 2**30)
    logging.debug(f'Timer successfully ended')
    duration = time.perf_counter() - time_start
    logging.info(f"Result of calculate_sum is {func_1}. Execution time: {duration:.3f}s")

    logging.debug(f'Timer successfully started')
    time_start = time.perf_counter()
    func_2 = calculate_sum_parallel(1, 2**30)
    logging.debug(f'Timer successfully ended')
    duration = time.perf_counter() - time_start
    logging.info(f"Result of calculate_sum_parallel is {func_2}. Execution time: {duration:.3f}s")

    if func_1 == func_2:
        logging.info("Both results are equal")
    else:
        logging.error("Please check the inputs in both calls")

    logging.debug(f'Timer successfully started')
    time_start = time.perf_counter()
    workload_total, workload_max = sleep_parallel()
    logging.debug(f'Timer successfully ended')
    duration = time.perf_counter() - time_start
    logging.info(
          f"Total workload time: {workload_total:.3f}s. " 
          f"Max workload time: {workload_max:.3f}s. "
          f"Execution time: {duration:.3f}s"
          )

if __name__ == "__main__":
    main()
