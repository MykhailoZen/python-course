import time
import random
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def calculate_sum(start: int, end: int):
    return sum(range(start, end + 1))


def calculate_sum_parallel(chunks_list):
    with Pool() as P:
        res = P.starmap(calculate_sum, chunks_list)
    all_sum = sum(res)
    return (f'{all_sum}')


if __name__ == '__main__':
    start = 1
    end = 2**30
    input = range(start, end + 1)
    n = 100000 # the bigger the n the less chunks we will have, thus the result will be faster
    chunks = [input[i:i + n] for i in range(0, len(input), n)]
    chunks_list = [(chunk_values[0], chunk_values[-1]) for chunk_values in chunks]

    start_1 = time.monotonic()
    print(calculate_sum_parallel(chunks_list))
    end_1 = time.monotonic()
    print("Time_1:", end_1 - start_1)
    print('-------')

    start_2 = time.monotonic()
    calculated = calculate_sum(start, end)
    print(calculated)
    end_2 = time.monotonic()
    print("Time_2:", end_2 - start_2)

#######


def sleep_func(amount):
    print(f"Sleep for {amount} seconds \n") #\n because it was overlapping when ran without it
    time.sleep(amount)
    return f"Sleep end {amount} seconds"


def run_sleep(amount):
    with ThreadPoolExecutor() as T:
        for _ in range(20):
            res = T.submit(sleep_func, amount)
            print(res.result())


if __name__ == '__main__':
    sleep_time = random.randint(1, 9)
    print(sleep_func(sleep_time))
    start_3 = time.monotonic()
    run_sleep(sleep_time)
    end_3 = time.monotonic()
    print("Time_3:", end_3 - start_3)
    # sorry, I am aware its unfinished