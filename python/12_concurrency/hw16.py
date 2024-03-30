
#Multiprocessing, CPU-bound work
#1.Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

print(calculate_sum(3, 6))


#Multithreading, IO-bound work
#1.Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

import random
import time

def random_sleep():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    return sleep_duration

print(random_sleep())