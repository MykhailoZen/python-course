import random
import time
import concurrent.futures
import logging

# Add logging to the code implemented in the "Concurrency" module.
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='logs.log', mode='w')

file_handler.setLevel(logging.INFO)

log_format = '%(asctime)s - %(levelname)s - %(message)s'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Multiprocessing, CPU-bound work
# 1
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


logging.info('Sum: %s', calculate_sum(1, 3))


# Multithreading, IO-bound work:
# 1

def random_sleep():
    sleep_duration = random.uniform(0, 10)
    logging.debug('Sleep duration: %s seconds', sleep_duration)
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
logging.info('Total results: %s', len(results))
