import concurrent.futures
import logging
import random
import time

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(process)d - %(thread)d - %(message)s',
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()


def random_sleep() -> float:
    sleep_duration = random.uniform(0, 10)
    time.sleep(sleep_duration)
    logger.debug(f"Slept for {sleep_duration:.2f} seconds")
    return sleep_duration


def parallel_random_sleep():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(random_sleep) for _ in range(20)]
        total_workload = 0
        max_workload = 0

        for future in concurrent.futures.as_completed(results):
            sleep_duration = future.result()
            total_workload += sleep_duration
            max_workload = max(max_workload, sleep_duration)

    logger.info(f"Total Workload: {total_workload:.2f} seconds")
    logger.info(f"Max Workload: {max_workload:.2f} seconds")


if __name__ == '__main__':
    start_time = time.time()
    parallel_random_sleep()
    elapsed_time = time.time() - start_time
    logger.info(f"Elapsed Time: {elapsed_time:.2f} seconds")
