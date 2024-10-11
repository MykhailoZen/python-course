from random import randrange

import multiprocessing
import time
import concurrent.futures

# Multiprocessing, CPU-bound work
#1. Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers
# in the given range including both ends.

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

print("Check no multiprocessing:", calculate_sum(1,50))

#2. Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.

def calculate_sum_parallel(start: int, end: int, num_processes: int = None) -> int:

    if num_processes is None:
        num_processes = multiprocessing.cpu_count()


    chunk_size = (end - start + 1) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    results = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_processes - 1 else end
        results.append(pool.apply_async(calculate_sum, (chunk_start, chunk_end)))

    pool.close()
    pool.join()

    total_sum = sum(result.get() for result in results)
    return total_sum

print("Check with multiprocessing:", calculate_sum_parallel(1,50))

#3. Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
#4. Print the times it takes for each approach.

start=time.time()
if calculate_sum(1, 2**30) == 576460752840294400:
    end=time.time()
    print("#1 No multiprocessing fits, it took", end-start, "s")
else:
    print("#1 No multiprocessing fail")


start=time.time()
if calculate_sum_parallel(1, 2**30) == 576460752840294400:
    end = time.time()
    print("#2 With multiprocessing fits, it took", end-start, "s")
else:
    print("#2 With multiprocessing fail")

# Multithreading, IO-bound work
#1. Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

def random_sleep(num):
    random_number=randrange(1,10)
    start=time.time()
    time.sleep(random_number)
    end=time.time()
    times.append(round(end-start,5))
    return end-start

#2. Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
#3. Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time
# (the longest task).
#4. Print the elapsed time. It should be several times smaller than the "workload" time.

calls = [n for n in range(20)]
times=[]

def threads_parallelization(sleep_func):
    print("\nStarting parallelization:")
    new_start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(sleep_func, calls)
    new_end = time.time()
    print("Number of iterations:", len(times))
    print("Elapsed time:", round(new_end-new_start,4),"s")
    print("Maximum workload:",max(times),"s")
    print("Total workload:", sum(times),"s")

threads_parallelization(random_sleep)