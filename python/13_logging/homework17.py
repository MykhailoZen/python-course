import logging
import math
import multiprocessing
import time

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(process)d - %(message)s',
    handlers=[logging.FileHandler('logfile.log'), logging.StreamHandler()],
)

logger = logging.getLogger()


def calculate_sum(start: int, end: int) -> int:
    if start > end:
        logger.error(
            'Invalid range. Start must be lesser than or equal to end'
        )
        return 0
    elif start == end:
        logger.warning(
            'start can\'t be equal to end. Empty range will be created'
        )
        return 0
    else:
        return sum(range(start, end + 1))


def calculate_sum_parallel(
    start: int, end: int, n_proc=multiprocessing.cpu_count()
) -> int:
    if start > end:
        logger.error('Invalid range. Start must be lesser than end')
        return 0
    elif start == end:
        logger.error(
            'Start can\'t be equal end for parallel method. Zero division occurred while trying to divide process on chunks'
        )
        return 0
    else:
        len_range = end - start + 1
        logger.debug(f"Length of range: {len_range}")
        chunk_size = int(len_range / n_proc)
        logger.debug(f"Chunk size: {chunk_size}")
        n_chunks = math.ceil(len_range / chunk_size)
        logger.debug(f"Number of chunks: {n_chunks}")

        ranges = []
        left = start
        for _ in range(0, n_chunks):
            ranges.append((left, min(end, left + chunk_size - 1)))
            left += chunk_size

        with multiprocessing.Pool(n_proc) as p:
            return sum(p.starmap(calculate_sum, ranges))


if __name__ == '__main__':
    n = 25
    start_time = time.time()
    logger.info(f"Sequential sum result: {calculate_sum(250, n)}")
    duration = time.time() - start_time
    logger.info(f'Sequential method took {duration} seconds')

    start_time = time.time()
    logger.info(f"Parallel sum result: {calculate_sum_parallel(250, n)}")
    duration = time.time() - start_time
    logger.info(f'Parallel method took {duration} seconds')
