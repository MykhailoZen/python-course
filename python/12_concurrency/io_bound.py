import time
import random
from concurrent.futures import ThreadPoolExecutor


def io_bound_task():
    """Simulates an IO-bound task by sleeping for a random amount of time (up to 10 seconds)."""
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    print(f"Task slept for {sleep_duration:.2f} seconds.")
    return sleep_duration


def run_parallel_tasks():
    """Runs multiple IO-bound tasks in parallel using ThreadPoolExecutor."""
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(io_bound_task) for _ in range(20)]

    workload_times = [result.result() for result in results]
    total_workload = sum(workload_times)
    max_workload = max(workload_times)

    print(f"\nTotal workload time: {total_workload:.2f} seconds.")
    print(f"Max workload time: {max_workload:.2f} seconds.")

    return workload_times


if __name__ == "__main__":
    start_time = time.time()
    workload_times = run_parallel_tasks()
    elapsed_time = time.time() - start_time

    print(f"\nElapsed time: {elapsed_time:.2f} seconds.")
