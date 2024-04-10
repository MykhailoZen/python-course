import multiprocessing
import time
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("logfile.log"),
                        logging.StreamHandler()
                    ])


# Function to calculate sum of numbers in a range sequentially
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


# Function to calculate sum of numbers in a range in parallel
def calculate_sum_parallel(start: int, end: int, num_processes: int = None) -> int:
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    chunk_size = (end - start + 1) // num_processes
    pool = multiprocessing.Pool(processes=num_processes)

    results = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_processes - 1 else end
        results.append(pool.apply_async(calculate_sum, (chunk_start, chunk_end)))

    pool.close()
    pool.join()

    total_sum = sum(result.get() for result in results)
    return total_sum


# Main function
def main():
    start = 1
    end = 2 ** 30  # Calculate sum of numbers from 1 to 2^30

    # Run the sequential function
    logging.info("Running sequential function...")
    start_time = time.time()
    result_sequential = calculate_sum(start, end)
    end_time = time.time()
    sequential_time = end_time - start_time
    logging.info("Sequential result: %s", result_sequential)
    logging.info("Sequential execution time: %s seconds", sequential_time)

    # Run the parallel function
    logging.info("\nRunning parallel function...")
    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    end_time = time.time()
    parallel_time = end_time - start_time
    logging.info("Parallel result: %s", result_parallel)
    logging.info("Parallel execution time: %s seconds", parallel_time)

    # Verify the results
    expected_result = 576460752840294400
    assert result_sequential == result_parallel == expected_result, "Results do not match"
    logging.info("\nResults match!")


# Entry point
if __name__ == "__main__":
    main()
