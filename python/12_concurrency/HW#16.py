import multiprocessing
import time
import asyncio
import random
import concurrent.futures
import threading

# Multiprocessing, CPU-bound work:


def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


def calculate_sum_partial(args):
    return calculate_sum(*args)


def calculate_sum_parallel(start: int, end: int) -> int:
    chunk_size = (end - start + 1) // multiprocessing.cpu_count()
    ranges = [(i, min(i + chunk_size - 1, end)) for i in range(start, end, chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sum_partial, ranges)

    return sum(results)


class Calculator:
    def __init__(self):
        pass


if __name__ == "__main__":
    calculator = Calculator()

    start_time = time.time()
    result_serial = calculate_sum(1, 2 ** 30)
    serial_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2 ** 30)
    parallel_time = time.time() - start_time

    print("Serial Result:", result_serial)
    print("Parallel Result:", result_parallel)
    print("Serial Time:", serial_time)
    print("Parallel Time:", parallel_time)


# Multithreading, IO-bound work:


def random_sleep() -> float:
    sleep_duration = random.random() * 10
    time.sleep(sleep_duration)
    thread_name = threading.current_thread().name
    print(f"Thread {thread_name} slept for {sleep_duration:.2f} seconds")
    return sleep_duration


def run_parallel_tasks():
    start_time = time.time()
    total_workload = 0
    max_workload = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]

        for future in concurrent.futures.as_completed(futures):
            sleep_duration = future.result()
            total_workload += sleep_duration
            if sleep_duration > max_workload:
                max_workload = sleep_duration

    elapsed_time = time.time() - start_time

    print("\nTotal Workload Time:", total_workload)
    print("Max Workload Time:", max_workload)
    print("Elapsed Time:", elapsed_time)


class TaskManager:
    def __init__(self):
        pass


if __name__ == "__main__":
    task_manager = TaskManager()
    run_parallel_tasks()


# (optional) asyncio practice:

async def random_sleep() -> float:
    sleep_duration = random.random() * 10
    await asyncio.sleep(sleep_duration)
    print(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration


async def run_parallel_tasks():
    start_time = time.time()
    total_workload = 0
    max_workload = 0

    tasks = [random_sleep() for _ in range(20)]
    completed_tasks = await asyncio.gather(*tasks)

    for sleep_duration in completed_tasks:
        total_workload += sleep_duration
        if sleep_duration > max_workload:
            max_workload = sleep_duration

    elapsed_time = time.time() - start_time

    print("\nTotal Workload Time:", total_workload)
    print("Max Workload Time:", max_workload)
    print("Elapsed Time:", elapsed_time)


class TaskManagerAsync:
    def __init__(self):
        pass


if __name__ == "__main__":
    task_manager_async = TaskManagerAsync()
    asyncio.run(run_parallel_tasks())
