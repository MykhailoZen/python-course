import concurrent.futures
import random
import time

def random_sleep():
    duration = random.uniform(0,10)
    time.sleep(duration)
    print(f"Slept for {duration:.2f} seconds")
    return duration


def parallel_calls():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]
        total_workload_time = 0
        max_workload_time = 0
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            total_workload_time += result
            if result > max_workload_time:
                max_workload_time = result

    return total_workload_time, max_workload_time

if __name__ == "__main__":
    start_time = time.time()
    total_workload_time, max_workload_time = parallel_calls()
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Total workload time: {total_workload_time:.2f} seconds")
    print(f"Max workload time: {max_workload_time:.2f} seconds")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
