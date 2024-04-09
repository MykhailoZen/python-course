import time
import multiprocessing
import logging
import sys
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define a function to configure logging to write INFO+ messages to a log file
def configure_file_logging(log_file):
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def calculate_sum(start: int, end: int) -> int:
    """Calculate the sum of numbers in the given range including both ends."""
    return sum(range(start, end+1))

def calculate_sum_parallel(start: int, end: int, chunk_size: int = 10**6) -> int:
    """Calculate the sum in parallel by splitting the range into chunks and utilizing multiprocessing."""
    num_chunks = (end - start + 1) // chunk_size
    chunks = [(start + i * chunk_size, min(start + (i+1) * chunk_size, end+1)) for i in range(num_chunks)]
    
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, chunks)
    
    return sum(results)

if __name__ == "__main__":
    # Configure logging to write INFO+ messages to a log file
    log_file = "sum_calculation.log"
    configure_file_logging(log_file)

    # Time the serial calculation
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time

    # Time the parallel calculation
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    parallel_time = time.time() - start_time

    # Log results and timings
    logger.info("Serial result: %s", result_serial)
    logger.info("Parallel result: %s", result_parallel)
    logger.info("Serial Time: %s", serial_time)
    logger.info("Parallel Time: %s", parallel_time)

    # Print results and timings
    print("Serial result:", result_serial)
    print("Parallel result:", result_parallel)
    print("Serial Time:", serial_time)
    print("Parallel Time:", parallel_time)

    # Close file handlers and remove if log file is empty
    for handler in logger.handlers:
        handler.close()
    if os.path.getsize(log_file) == 0:
        os.remove(log_file)
