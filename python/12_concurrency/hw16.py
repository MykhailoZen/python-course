import concurrent.futures
import random
import time
from time import sleep
import multiprocessing

"""
Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of 
numbers in the given range including both ends.
Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner 
(e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
Split the given range into chunks, obtain the result for each range chunk, 
and return the total sum. The returning result should be the same as for the first function.
Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
Print the times it takes for each approach.
"""

def calculate_sum(start: int, end: int) -> int:
    return sum(range(end + 1))

def calculate_sum_parallel(start: int, end: int, chunk_size: int = 10000) -> int:
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    with multiprocessing.Pool() as pool:
        result = pool.starmap(calculate_sum, chunks)

    return sum(result)


if __name__ == '__main__':

    start_time = time.time()
    result_sequential = calculate_sum(1, 2 ** 30)
    seq_time = time.time() - start_time
    result_parallel = calculate_sum_parallel(1, 2 ** 30)
    parallel_time = time.time() - start_time

    print(f"SUM IS: {result_sequential}")
    print(f"Sequentially: {seq_time} sec")
    print("VS")
    print(f"SUM IS: {result_parallel}")
    print(f"Parallel: {parallel_time} sec")


"""
Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
Create another function that calls the previous one 20 times using multiple threads in parallel 
(e.g. use "concurrent.futures.ThreadPoolExecutor" class).
Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
Print the elapsed time. It should be several times smaller than the "workload" time.
"""

def sleeping(*args):
    starttime = time.time()
    sec = random.randint(1, 10)
    print(f"Sleeping for {sec} seconds")
    sleep(sec)
    worktime = time.time() - starttime
    return worktime

start = time.time()
total_workload_time = 0
max_workload_time = 0


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
    results = pool.map(sleeping, [None] * 20)
    for duration in results:
        total_workload_time += duration
        if duration > max_workload_time:
            max_workload_time = duration


print(f'Elapsed time using concurrency : {time.time() - start:.3f} sec')
print(f'Total workload time without concurrency could be : {total_workload_time:.3f} sec')
print(f'The max workload time was: {max_workload_time:.3f} sec')

