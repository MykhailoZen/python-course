import concurrent.futures
import random
import time
from time import sleep
import logging


logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG)
# test
logging.warning('Logging started')
handler = logging.FileHandler("Logs.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(processName)s "
                              "- %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)


def sleeping(*args):
    starttime = time.time()
    sec = random.randint(1, 10)
    print(f"Sleeping for {sec} seconds")
    sleep(sec)
    worktime = time.time() - starttime
    return worktime


start = time.time()
total_workload_time = 0
max_workload_time = 0


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
    results = pool.map(sleeping, [None] * 1)
    for duration in results:
        total_workload_time += duration
        if duration > max_workload_time:
            max_workload_time = duration


logging.debug(f'Elapsed time using concurrency : '
              f'{time.time() - start:.3f} sec')
logging.critical(f'Total workload time without concurrency could be : '
                 f'{total_workload_time:.3f} sec')
logging.info(f'The max workload time was: {max_workload_time:.3f} sec')
logging.error('Finished! Verified with the Flake8 editor')
