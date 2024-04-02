""" Multithreading, IO-bound work (30 points):
- Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
- Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
- Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
- Print the elapsed time. It should be several times smaller than the "workload" time.
"""

import time
import random
import concurrent.futures

def random_sleep() -> float:
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    print(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration

def parallel_random_sleep():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(random_sleep) for _ in range(20)]
        total_workload = 0
        max_workload = 0

        for future in concurrent.futures.as_completed(results):
            sleep_duration = future.result()
            total_workload += sleep_duration
            max_workload = max(max_workload, sleep_duration)

    print(f"Total Workload: {total_workload:.2f} seconds")
    print(f"Max Workload: {max_workload:.2f} seconds")

if __name__ == '__main__':
    start_time = time.time()
    parallel_random_sleep()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")