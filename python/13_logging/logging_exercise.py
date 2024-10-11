import concurrent.futures
import logging
import os
import time
from random import randrange

# 1. Add logging to the code implemented in the "Concurrency" module ...
# (and so on)

if os.path.exists("logfile.log"):
    os.remove("logfile.log")

logger = logging.getLogger()
logger.setLevel("DEBUG")
formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{")

console_handler = logging.StreamHandler()
console_handler.setLevel("INFO")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("logfile.log", mode="a", encoding="utf-8")
file_handler.setLevel("DEBUG")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

calls = [n for n in range(20)]
logger.debug("Creating tables...")
times = []


def random_sleep(num):
    random_number = randrange(1, 10)
    starting_time = time.time()
    time.sleep(random_number)
    end_time = time.time()
    times.append(round(end_time - starting_time, 5))
    return end_time - starting_time


def threads_parallelization(sleep_func):
    logging.info("Starting parallelization...")
    logger.debug("Setting time...")
    new_start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(sleep_func, calls)
    logger.debug("Subtracting time")
    new_end = time.time()
    logger.info("Number of iterations: %s", len(times))
    logger.info("Elapsed time: %s s", round(new_end - new_start, 4))
    logger.info("Maximum workload: %s s", max(times))
    logger.info("Total workload: %s s", sum(times))


threads_parallelization(random_sleep)
