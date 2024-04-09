import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("gpu.log", mode="w"),
    ],
)

logging.getLogger().handlers[1].setLevel(logging.INFO)  # File


def random_sleep():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    logging.debug(f"Duration is {sleep_duration:.2f} seconds.")
    return sleep_duration


def random_sleep_many(number):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(number)]
        results = [future.result() for future in futures]
    total_workload_time = sum(results)
    max_workload_time = max(results)
    elapsed_time = time.time() - start_time
    return total_workload_time, max_workload_time, elapsed_time


if __name__ == "__main__":

    random_sleep()

    total_workload, max_workload, elapsed_time = random_sleep_many(20)
    logging.info(f"Total workload time is {total_workload:.2f} seconds")
    logging.info(f"Max workload time is {max_workload:.2f} seconds")
    logging.info(f"Elapsed time is {elapsed_time:.2f} seconds")
    print()
