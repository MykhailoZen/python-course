# Multithreading, IO-bound work
import time
import random
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("concurrency.log", mode='w'),
                              logging.StreamHandler()])

def random_sleep():
    sleep_time = random.uniform(0, 10)
    time.sleep(sleep_time)
    logging.info(f"Slept for {sleep_time:.2f} seconds.")
    return sleep_time

def execute_in_parallel():
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda _: random_sleep(), range(20)))

    total_workload = sum(results)
    max_workload = max(results)
    logging.info(f"Total workload time: {total_workload:.2f} seconds.")
    logging.info(f"Max workload time: {max_workload:.2f} seconds.")

if __name__ == "__main__":
    start_time = time.monotonic()
    execute_in_parallel()
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    logging.info(f"Elapsed time: {elapsed_time:.2f} seconds.")