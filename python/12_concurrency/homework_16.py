# Multiprocessing, CPU-bound work
import random
import concurrent.futures
import time
import multiprocessing


def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


def calculate_sum_parallel(start: int, end: int, num_processes: int) -> int:
    chunk_size = (end - start + 1) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    results = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_processes - 1 else end
        results.append(pool.apply_async(calculate_sum, (chunk_start, chunk_end)))
    total_sum = sum(result.get() for result in results)
    pool.close()
    pool.join()
    return total_sum


if __name__ == "__main__":
    start_time = time.time()
    result_single = calculate_sum(1, 2 ** 30)
    single_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2 ** 30, multiprocessing.cpu_count())
    parallel_time = time.time() - start_time

    print("Single Process Result:", result_single)
    print("Parallel Process Result:", result_parallel)
    print("Single Process Time:", single_time)
    print("Parallel Process Time:", parallel_time)


# Multithreading, IO-bound work:

def random_sleep():
    sleep_duration = random.uniform(0, 10)
    print('Sleep duration:', sleep_duration, 'seconds')
    time.sleep(sleep_duration)
    return sleep_duration


def call_random_sleep_multiple_times():
    start_time_inner = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]
        total_workload_time = 0
        max_workload_time = 0
        for future in concurrent.futures.as_completed(futures):
            sleep_duration = future.result()
            total_workload_time += sleep_duration
            max_workload_time = max(max_workload_time, sleep_duration)

    elapsed_time = time.time() - start_time_inner
    print("Total workload time:", total_workload_time)
    print("Max workload time:", max_workload_time)
    print("Elapsed time:", elapsed_time)


if __name__ == "__main__":
    call_random_sleep_multiple_times()
