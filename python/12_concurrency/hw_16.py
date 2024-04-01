import threading
import time
import queue
import multiprocessing
import math

my_queue = queue.Queue()

# Determine the number of available CPU cores
num_processes = multiprocessing.cpu_count()

# Multiprocessing, CPU-bound work (30 points):
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.

start = 1
end = 2 ** 30 + 1

numbers_per_interval = (end - start + 1) // num_processes
ranges = [(start + i * numbers_per_interval, start + (i + 1) * numbers_per_interval) for i in range(num_processes)]
ranges[-1] = (ranges[-1][0], end)


def time_execution_decorator(func):
    def timer(*args, **kwargs):
        start_execution = time.time()
        func(*args, **kwargs)
        end_execution = time.time()

        execution_time = end_execution - start_execution
        execution_time_milliseconds = end_execution - start_execution * 1000
        milliseconds = int(execution_time_milliseconds % 1000)
        time_formatted = time.strftime('%H:%M:%S', time.gmtime(execution_time)) + f'.{milliseconds:03d}'

        print(f'Time taken for execution: {time_formatted}')
    return timer


def calculate_sum(start_range, end_range):
    result = sum(range(start_range, end_range))
    my_queue.put(result)
    return result


@time_execution_decorator
def threading_calculated_sum():
    print("Threading execution: ")

    threads = []
    for r in ranges:
        t = threading.Thread(target=calculate_sum, args=r)
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = 0
    while not my_queue.empty():
        total_sum += my_queue.get()

    print(total_sum)


# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum"
# in a parallel manner
# (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").


@time_execution_decorator
def multiprocessing_calculated_sum():
    print("Multiprocessing execution: ")

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(calculate_sum, ranges)

    total_sum = sum(results)

    print(total_sum)


if __name__ == '__main__':
    threading_calculated_sum()
    print('')
    multiprocessing_calculated_sum()

# The returning result should be the same as for the first function.
# Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
# Print the times it takes for each approach.


# Multithreading, IO-bound work (30 points):
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
# Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.
