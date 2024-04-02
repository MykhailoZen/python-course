import time
import multiprocessing

def calculate_sum(start: int, end: int) -> int:
    """Calculate the sum of numbers in the given range including both ends."""
    return sum(range(start, end+1))

def calculate_sum_parallel(start: int, end: int, chunk_size: int = 10**6) -> int:
    """Calculate the sum in parallel by splitting the range into chunks and utilizing multiprocessing."""
    # Determine the number of chunks based on the chunk size
    num_chunks = (end - start + 1) // chunk_size
    # Create a list of tuples representing the chunks
    chunks = [(start + i * chunk_size, min(start + (i+1) * chunk_size, end+1)) for i in range(num_chunks)]
    
    # Use multiprocessing to calculate the sum for each chunk in parallel
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, chunks)
    
    # Return the total sum of all chunk results
    return sum(results)

if __name__ == "__main__":
    # Time the serial calculation
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time

    # Time the parallel calculation
    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30)
    parallel_time = time.time() - start_time

    # Print results and timings
    print("Serial result:", result_serial)
    print("Parallel result:", result_parallel)
    print("Serial Time:", serial_time)
    print("Parallel Time:", parallel_time)
