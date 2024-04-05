"""Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
Create another function that calls the previous one 20 times using multiple threads in parallel
(e.g. use "concurrent.futures.ThreadPoolExecutor" class).
Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
Print the elapsed time. It should be several times smaller than the "workload" time.
"""

from random import randint
import concurrent.futures
import time
import statistics

def sleep_random():
    sleep_time = randint(0, 20)
    time.sleep(sleep_time)
    return sleep_time

def main_task():
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        result = [executor.submit(sleep_random) for _ in range(20)]
    for x in result:
        results.append((x.result()))
    print("all results: ", results )
    max_results = (max(results))
    print("max time: ", max_results)
    avg_results = statistics.mean(results)
    print("avg time: ", avg_results)

if __name__ == "__main__":
    start_time = time.time()
    run_main = main_task()
    print("total time:", round(time.time() - start_time, 2), "seconds\n")

