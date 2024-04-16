import concurrent.futures
import time
import random

def sleep_random():
    """Sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration."""
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)
    print(f"Slept for {sleep_time} seconds.")
    return sleep_time

def execute_in_threads():
    """Calls the sleep_random function 20 times using multiple threads."""
    total_workload_time = 0
    max_workload_time = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(sleep_random) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            sleep_duration = future.result()
            total_workload_time += sleep_duration
            max_workload_time = max(max_workload_time, sleep_duration)

    print(f"Total workload time: {total_workload_time} seconds.")
    print(f"Max workload time: {max_workload_time} seconds.")

if __name__ == "__main__":
    start_time = time.time()
    execute_in_threads()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds.")
