import random
import time
import multiprocessing
import concurrent.futures


# Create a function (e.g. "calculate_sum(start: int, end: int) -> int")
# which returns the sum of numbers in the given range including both ends.

def calculate_sum(start: int, end: int) -> int:

    res = 0
    for i in range(start, end+1):
        res += i
    return res


# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor").
# Split the given range into chunks, obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.
def calculate_sum_parallel(start: int, end: int) -> int:

    num_chunks = multiprocessing.cpu_count()
    chunk_size = (end - start + 1) // num_chunks
    chunks = [(i, min(i + chunk_size - 1, end)) for i in range(start, end + 1, chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, chunks)

    return sum(results)


def sleep_randomiser():
    sleep_dur = random.random() * 10
    time.sleep(sleep_dur)
    return sleep_dur

def sleep_parallel():
    workload_total = 0
    workload_max = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_randomiser) for _ in range(20)]

        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            workload_total += result
            workload_max = max(workload_max, result)

    return workload_total, workload_max


def main():

    time_start = time.perf_counter()
    func_1 = calculate_sum(1, 2**30)
    duration = time.perf_counter() - time_start
    print(f"Result of calculate_sum is {func_1}. Execution time: {duration: .3f}s")

    time_start = time.perf_counter()
    func_2 = calculate_sum_parallel(1, 2**30)
    duration = time.perf_counter() - time_start
    print(f"Result of calculate_sum_parallel is {func_2}. Execution time: {duration: .3f}s")

    if func_1 == func_2:
        print("Both results are equal")
    else:
        raise ValueError("Please check the inputs in both calls")

    time_start = time.perf_counter()
    workload_total, workload_max = sleep_parallel()
    duration = time.perf_counter() - time_start
    print(f"Total workload time: {workload_total: .3f}s. " 
          f"Max workload time: {workload_max: .3f}s. "
          f"Execution time: {duration: .3f}s"
          )

if __name__ == "__main__":
    main()

