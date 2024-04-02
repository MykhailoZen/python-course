import multiprocessing
import time
import random
import concurrent.futures


def calculate_sum(start: int, end: int) -> int:
    """
    Function returns the sum of numbers in the given range including both ends
    :param start: start of numbers range
    :param end: end of numbers range
    :return: sum of numbers is range
    """
    return sum(range(start, end+1))


def calculate_sum_parallel(start: int, end: int, n: int = 50000) -> int:
    """
    Function returns the sum of numbers in the given range including both ends in a parallel manner
    :param start: start of numbers range
    :param end: end of numbers range
    :param n: size of chunk, default = 50000
    :return: sum of numbers is range
    """
    chunk = [(i, min(i + n - 1, end)) for i in range(start, end + 1, n)]
    with multiprocessing.Pool() as pool:
        iteration = pool.starmap(calculate_sum, chunk)

    return sum(iteration)


def sleep_time() -> int:
    """
    Function that sleeps for a random amount of time
    :return: sleeping duration
    """
    time_sleep = random.randint(1, 10)
    time.sleep(time_sleep)
    return time_sleep


def threads_sleep_time():
    """
    Function that calls the sleep_time function 20 times using multiple threads in parallel.
    Prints the sum of outputs from all calls and the time of longest task.
    """
    total_workload = 0
    max_workload = 0
    with concurrent.futures.ThreadPoolExecutor() as pool:
        results = [pool.submit(sleep_time) for _ in range(20)]
        concurrent.futures.wait(results)
        for n in results:
            time_sleep = n.result()
            total_workload += time_sleep
            max_workload = max(max_workload, time_sleep)

    print(f'Total workload time of all threads {total_workload} seconds, max workload time {max_workload} seconds')


if __name__ == '__main__':
    start_time = time.time()
    calculate_sum(1, 2 ** 30)
    duration = time.time() - start_time
    print(f'Calculation without multiprocessing takes {duration:.3f} seconds')

    start_time = time.time()
    calculate_sum_parallel(1, 2 ** 30)
    duration = time.time() - start_time
    print(f'Calculation with multiprocessing takes {duration:.3f} seconds')

    print(f'Random sleep time function takes {sleep_time()} seconds')

    start_time = time.time()
    threads_sleep_time()
    elapsed_duration = time.time() - start_time
    print(f'Function elapsed duration with threads {elapsed_duration:.3f} seconds')
