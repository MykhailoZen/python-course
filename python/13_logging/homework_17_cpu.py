import logging
import multiprocessing
import time

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create console handler and set level to DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Create file handler and set level to INFO
file_handler = logging.FileHandler('logfile.log')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end+1))


def chunk_range(start: int, end: int, num_chunks: int) -> list:
    chunk_size = (end - start + 1) // num_chunks
    chunks = []
    logging.debug(f"{chunk_size=}")
    logging.debug(f"{num_chunks=}")

    for i in range(num_chunks):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_chunks - 1 else end
        chunks.append((chunk_start, chunk_end))
    return chunks


def calculate_sum_parallel(start: int, end: int, num_processes: int) -> int:
    chunks = chunk_range(start, end, num_processes)
    logging.debug(f"{num_processes=}")
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(calculate_sum, chunks)
    return sum(results)


if __name__ == "__main__":
    logging.info("Starting serial calculation...")
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time
    logging.info("Serial calculation completed in %.4f seconds.", serial_time)

    logging.info("Starting parallel calculation...")
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30,
                                             multiprocessing.cpu_count())
    parallel_time = time.time() - start_time
    logging.info("Parallel calculation completed in %.4f seconds.",
                 parallel_time)

    logging.info("Serial Result: %s", result_serial)
    logging.info("Parallel Result: %s", result_parallel)
    logging.info("Serial Time: %.4f seconds", serial_time)
    logging.info("Parallel Time: %.4f seconds", parallel_time)

    # Verify the result:
    expected_result = 576460752840294400
    if result_serial == result_parallel == expected_result:
        logging.info("Results verified!")
    else:
        logging.error("Results verification failed!")
