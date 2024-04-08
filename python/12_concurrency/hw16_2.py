
#Multiprocessing, CPU-bound work
#1.Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.

def calculate_sum(start: int, end: int):
    return sum(range(start, end + 1))

print(f"Task_1 with 3, 6 values: {calculate_sum(3, 6)}")


#Multithreading, IO-bound work
#1.Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

import random
import time

def random_sleep():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    return sleep_duration

print(f"Task_2: {random_sleep()} secs")


#2.Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).

import concurrent.futures

def run_random_sleep_multiple_times():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(f"Task_3: {result} secs")

run_random_sleep_multiple_times()