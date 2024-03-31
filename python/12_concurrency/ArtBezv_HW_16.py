#Multithreading, IO-bound work

import concurrent.futures
import time
import random

def sleep_random():

    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    print(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration

def sleep_random_in_parallel():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(sleep_random) for _ in range(20)]
        sleep_durations = [future.result() for future in concurrent.futures.as_completed(futures)]

        total_workload_time = sum(sleep_durations)
        max_workload_time = max(sleep_durations)

        print("Total workload time:", total_workload_time)
        print("Max workload time:", max_workload_time)


start_time = time.time()
sleep_random_in_parallel()
elapsed_time = time.time() - start_time
print("Elapsed time:", elapsed_time)
