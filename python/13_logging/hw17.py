
#Add logging to the code implemented in the "Concurrency" module.
# - There should be at least two logging levels: debug and info.
# - All print statements should be replaced with logging.
# - Configure logging to print all log messages to the console, and write INFO+ messages to a log file.

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s : %(levelname)s : %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("hw17_logging.log", mode='w')
    ]
)


#Multiprocessing, CPU-bound work
#1.Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.

def calculate_sum(start: int, end: int):
    logging.info("Task_1 started")
    logging.debug(f"Range of numbers: {start}, {end}")
    calculation = sum(range(start, end + 1))
    logging.debug(f"The sum of numbers in the given range: {calculation}")
    logging.info("Task_1 ended")
    return calculation

calculate_sum(3, 6)


#Multithreading, IO-bound work
#1.Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

import random
import time

def random_sleep():
    logging.info("Task_2 is running")
    sleep_duration = random.uniform(0, 10)
    logging.debug("Time duration range: 0, 10")
    time.sleep(sleep_duration)
    logging.debug(f"Random sleep duration: {sleep_duration}")
    logging.info("Task_2 ended")
    return sleep_duration

random_sleep()


#2.Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).

import concurrent.futures

def run_random_sleep_multiple_times():
    logging.info("Task_3 started")
    logging.debug("Create a ThreadPoolExecutor with 5 threads")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        logging.debug("Submit random_sleep() function 20 times")
        futures = [executor.submit(random_sleep) for _ in range(20)]
        logging.debug("Get the results as they complete")
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            logging.debug(f"Thread completed. Slept for {result} seconds")
    logging.info("Task_3 ended")

run_random_sleep_multiple_times()