# Dupilicate a 'concurency' task with a Loging and Code Style implementation

import concurrent.futures
import logging
import random
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

logging.getLogger("").addHandler(file_handler)


def sleep_random():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    logging.debug(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration


def sleep_random_in_parallel():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(sleep_random) for _ in range(20)]
        sleep_durations = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]

        total_workload_time = sum(sleep_durations)
        max_workload_time = max(sleep_durations)

        logging.info("Total workload time: %.2f", total_workload_time)
        logging.info("Max workload time: %.2f", max_workload_time)


start_time = time.time()
sleep_random_in_parallel()
elapsed_time = time.time() - start_time
logging.info("Elapsed time: %.2f seconds", elapsed_time)
