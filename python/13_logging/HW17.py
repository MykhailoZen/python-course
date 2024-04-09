import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("log.log", mode="w"), logging.StreamHandler()],
)


def calculate_sum(start: int, end: int):
    return sum(range(start, end + 1))


def calculate_sum_parallel(chunks_list):
    with Pool() as P:
        res = P.starmap(calculate_sum, chunks_list)
    all_sum = sum(res)
    return f"{all_sum}"


if __name__ == "__main__":
    start = 1
    end = 2**30
    input = range(start, end + 1)
    n = 100000
    chunks = [input[i : i + n] for i in range(0, len(input), n)]
    chunks_list = [(chunk_values[0], chunk_values[-1]) for chunk_values in chunks]

    start_1 = time.monotonic()
    logging.debug(f"Parallel calculation result: {calculate_sum_parallel(chunks_list)}")
    end_1 = time.monotonic()
    logging.debug(f"Time_1: {end_1 - start_1}")
    logging.info(f"Time it took to execute calculation: {end_1} - {start_1}")
    logging.info("In progress...")

    start_2 = time.monotonic()
    calculated = calculate_sum(start, end)
    logging.debug(f"Calculated: {calculated}")
    end_2 = time.monotonic()
    logging.debug(f"Time_2: {end_2 - start_2}")
    logging.info(f"Time it took to execute calculation #2: {end_2} - {start_2}")

#######


def sleep_func(amount):
    logging.info(f"Sleep for {amount} seconds \n")
    time.sleep(amount)
    return f"Sleep end {amount} seconds"


def run_sleep(amount):
    with ThreadPoolExecutor() as T:
        for _ in range(20):
            res = T.submit(sleep_func, amount)
            logging.debug(f"Result of run_sleep method: {res.result()}")


if __name__ == "__main__":
    sleep_time = random.randint(1, 9)
    logging.debug(f"Sleep time: {sleep_func(sleep_time)}")
    start_3 = time.monotonic()
    run_sleep(sleep_time)
    end_3 = time.monotonic()
    logging.info(f"Time_3: {end_3 - start_3}")
    logging.info(f"Time it took to execute sleep: {end_3 - start_3}")
