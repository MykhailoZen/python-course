import concurrent.futures
import random
import threading
import time


def calculate_sum(start: int, end: int):
    value = sum(range(start, end + 1))
    return value


def calculate_sum_chunk(chunk):
    return calculate_sum(*chunk)


def calculate_sum_parallel(start: int, end: int, chunk_size: int = 1000):

    result = 0
    chunks = [(i, min(i + chunk_size, end + 1)) for i in range(start, end + 1, chunk_size)]
    with concurrent.futures.ProcessPoolExecutor() as pool:
        results = pool.map(calculate_sum_chunk, chunks)
        result = sum(results)
    return result


if __name__ == '__main__':
    start = 1
    end = 2 ** 30

    start_time = time.time()
    result_serial = calculate_sum(start, end)
    print(result_serial)
    print(f'Time spent: {(time.time() - start_time):.2f}')

    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    print(result_parallel)
    print(f'Time spent: {(time.time() - start_time):.2f}')


def sleep_random():
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    print(f"Thread {threading.current_thread().name} slept for {sleep_duration:.2f} seconds")
    return sleep_duration


def run_tasks_parallel():
    total_workload_time = 0
    max_workload_time = 0
    with concurrent.futures.ThreadPoolExecutor() as pool:
        futures = [pool.submit(sleep_random) for _ in range(10)]
        for future in concurrent.futures.as_completed(futures):
            sleep_duration = future.result()
            total_workload_time += sleep_duration
            max_workload_time = max(max_workload_time, sleep_duration)
    print(f"Total workload time: {total_workload_time:.2f} seconds")
    print(f"Max workload time: {max_workload_time:.2f} seconds")


if __name__ == "__main__":
    start_time = time.time()
    run_tasks_parallel()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
