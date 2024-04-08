import concurrent.futures
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(filename="app.log", mode="w"),
    ],
)
logger = logging.getLogger(__name__)
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))
def calculate_sum_parallel(start: int, end: int, num_chunks: int = 4) -> int:
    chunk_size = (end - start + 1) // num_chunks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(num_chunks):
            chunk_start = start + i * chunk_size
            chunk_end = min(start + (i + 1) * chunk_size - 1, end)
            futures.append(executor.submit(calculate_sum, chunk_start, chunk_end))
        total_sum = sum(
            future.result() for future in concurrent.futures.as_completed(futures)
        )
    return total_sum


if __name__ == "__main__":
    start = 1
    end = 2**30
    start_time = time.time()
    result_normal = calculate_sum(start, end)
    elapsed_time = time.time() - start_time
    logger.info(f"The sum from {start} to {end} (normal): {result_normal}")
    logger.info(f"Total workload time: {elapsed_time:.2f} seconds")

    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    elapsed_time = time.time() - start_time
    logger.info(f"The sum from {start} to {end} (parallel): {result_parallel}")
    logger.info(f"Total workload time: {elapsed_time:.2f} seconds")
    logger.info("Results are the same: %s", result_normal == result_parallel)
