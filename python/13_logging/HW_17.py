import concurrent.futures
import logging
import multiprocessing
import random
import time


# Setting up DEBUG+ logging level. with console output
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Setting up INFO+ logging level with output to file
handler = logging.FileHandler("log_hw_17.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(processName)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logging.getLogger().addHandler(handler)

# Multiprocessing, CPU-bound work (30 points):
# 1. Create a function
# (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers
# in the given range including both ends.


def calculate_sum(start: int, end: int) -> int:
    logging.debug(f"Starting calculation for range {start}-{end}")
    result = sum(range(start, end + 1))
    logging.debug(f"Calculation completed for range {start}-{end}")
    logging.info(f"Sum calculated for range {start}-{end}: {result}")
    return result


# 2. Create another function (e.g. "calculate_sum_parallel")
# that calls "calculate_sum"
# in a parallel manner (e.g. using "multiprocessing.Pool"
# or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result
# for each range chunk, and return the total sum.
# The returning result should be the same
# as for the first function.


def calculate_sum_parallel(
    start: int, end: int, chunk_size: int = 1000000
) -> int:
    chunks = [
        (i, min(i + chunk_size - 1, end))
        for i in range(start, end + 1, chunk_size)
    ]

    logging.debug(f"Creating chunks: {chunks}")

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(calculate_sum, chunks)
    total_sum = sum(results)
    logging.info(f"Total sum calculated: {total_sum}")
    return total_sum


# Multithreading, IO-bound work (30 points):
# Create a function that sleeps for a random
# amount of time (<10 seconds), prints
# and returns the sleep duration.


def waste_time():
    sleep_time = random.uniform(1, 10)
    logging.debug(f"Starting waste_time with sleep time: {sleep_time}")
    time.sleep(sleep_time)
    logging.debug("Finished waste_time")
    return sleep_time


# Create another function that calls the previous one 20 times using
# multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls)
# and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than
# the "workload" time.


def parallel_waste_time():
    total_workload = 0
    max_workload = 0

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = [pool.submit(waste_time) for i in range(20)]
        concurrent.futures.wait(futures)
        for future in futures:
            sleep_time = future.result()
            total_workload += sleep_time
            max_workload = max(max_workload, sleep_time)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(
        f"Total workload (sum of results of all calls): {total_workload}"
    )
    logging.info(f"Maximum workload (longest task): {max_workload}")
    logging.info(f"Total elapsed task execution time: {elapsed_time}")
    return total_workload, max_workload, elapsed_time


if __name__ == "__main__":
    logging.info("Example of Multiprocessing, CPU-bound work:")
    # 3. Run both functions for the range [1, 2**30],
    # verify the result is 576460752840294400.
    # Print the times it takes for each approach.
    start_time = time.time()
    result_sequential = calculate_sum(1, 2**30)
    sequential_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    parallel_time = time.time() - start_time

    logging.info(
        f"calculating the sum of numbers sequentially: {result_sequential}"
    )
    logging.info(
        f"time to calculate the sum sequentially: {sequential_time} sec"
    )
    logging.info(f"calculating the sum of numbers parallel: {result_parallel}")
    logging.info(f"time to calculate the sum in parallel: {parallel_time} sec")

    if result_sequential == result_parallel == 576460752840294400:
        logging.info("Calculated result the same.")

    logging.info("Example of Multithreading, IO-bound work:")
    parallel_waste_time()
