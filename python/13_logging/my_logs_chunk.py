import concurrent.futures
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="logging_in.log",
                    filemode="a")  # with 'w' mode shows Null values

logging.debug("debug")
logging.info("info")


def calculate_sum(start: int, end: int):
    value = sum(range(start, end + 1))
    logging.info(value)
    logging.debug(value)
    return value


def calculate_sum_chunk(chunk):
    start, end = chunk
    logging.info(f"{start}, {end}")
    result = calculate_sum(start, end)
    logging.info(result)
    return result


def calculate_sum_parallel(start: int, end: int, chunk_size: int = 1000):
    result = 0
    chunks = [(i, min(i + chunk_size, end + 1)) for i in range(start, end + 1, chunk_size)]
    logging.info(chunks)
    with concurrent.futures.ProcessPoolExecutor() as pool:
        results = pool.map(calculate_sum_chunk, chunks)
        logging.info(results)
        result = sum(results)
        logging.info(result)
    return result


if __name__ == '__main__':
    start = 1
    end = 2 ** 15

    start_time = time.time()
    result_serial = calculate_sum(start, end)
    logging.info(f"Serial result: {result_serial}")
    logging.info(f'Time spent: {(time.time() - start_time):.2f}')

    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    logging.info(f"Parallel result: {result_parallel}")
    logging.info(f'Time spent: {(time.time() - start_time):.2f}')