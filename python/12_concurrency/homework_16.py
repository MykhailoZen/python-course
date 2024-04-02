import random
import time
import concurrent.futures


# Multiprocessing, CPU-bound work
# 1
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


print(calculate_sum(1, 3))


# Multithreading, IO-bound work (30 points):
# 1

def random_sleep():
    sleep_duration = random.uniform(0, 10)
    print('Sleep duration', sleep_duration, 'seconds')
    time.sleep(sleep_duration)
    return sleep_duration


random_sleep()


# 2

def call_random_sleep_multiple_times():
    local_results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(random_sleep) for _ in range(20)]
        for future in concurrent.futures.as_completed(futures):
            local_results.append(future.result())
    return local_results

results = call_random_sleep_multiple_times()
print("Total results:", len(results))
