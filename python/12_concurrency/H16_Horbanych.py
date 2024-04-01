
import time
import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

# Multiprocessing, CPU-bound work
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
def calculate_sum(start: int, end: int) -> int:
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.
def calculate_sum_parallel(start: int, end: int) -> int:
    chunk_size = (end - start + 1) // cpu_count()
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]
    with ProcessPoolExecutor() as executor:
        partial_sums = executor.map(calculate_sum, [chunk_start for chunk_start, _ in chunks],
                                    [chunk_end for _, chunk_end in chunks])
    return sum(partial_sums)


#Run both functions for the range [1, 2**30]
if __name__ == "__main__":
    target_range = (1, 2 ** 30)


    start_time = time.time()
    single_process_sum = calculate_sum(*target_range)
    end_time = time.time()
    single_process_time = end_time - start_time

    start_time = time.time()
    parallel_sum = calculate_sum_parallel(*target_range)
    end_time = time.time()
    parallel_time = end_time - start_time


#Print the times it takes for each approach.
    print(f"Single process sum: {single_process_sum}")
    print(f"Single process duration: {single_process_time:.4f} seconds")
    print(f"Parallel sum: {parallel_sum}")
    print(f"Parallel duration: {parallel_time:.4f} seconds\n\n")



# Multithreading, IO-bound work
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.

def io_bound_task():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    print(f"Task slept for {sleep_duration:.2f} seconds.")
    return sleep_duration

#Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).

def run_parallel_tasks():
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(io_bound_task) for _ in range(20)]

    workload_times = [result.result() for result in results]
    total_workload = sum(workload_times)
    max_workload = max(workload_times)

#Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
    print(f"\nTotal workload time: {total_workload:.2f} seconds.")
    print(f"Max workload time: {max_workload:.2f} seconds.")

    return workload_times

#P rint the elapsed time. It should be several times smaller than the "workload" time.
if __name__ == "__main__":
    start_time = time.time()
    workload_times = run_parallel_tasks()
    elapsed_time = time.time() - start_time

    print(f"\nElapsed time: {elapsed_time:.2f} seconds.")