"""Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.
Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (e.g. using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be the same as for the first function.
Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
Print the times it takes for each approach."""
import concurrent.futures
import time

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end+1))

def calculate_sum_parallel(start: int, end: int, num_chunks: int = 4) -> int:
    chunk_size = (end - start + 1) // num_chunks
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(num_chunks):
            chunk_start = start + i * chunk_size
            chunk_end = min(start + (i + 1) * chunk_size - 1, end)
            futures.append(executor.submit(calculate_sum, chunk_start, chunk_end))
        total_sum = sum(future.result() for future in concurrent.futures.as_completed(futures))
    return total_sum

if __name__ == "__main__":
    start = 1
    end = 2**30
    start_time = time.time()
    result_normal = calculate_sum(start, end)
    elapsed_time = time.time() - start_time
    print(f"The sum from {start} to {end} (normal): {result_normal}")
    print(f"Total workload time: {elapsed_time:.2f} seconds")

    start_time = time.time()
    result_parallel = calculate_sum_parallel(start, end)
    elapsed_time = time.time() - start_time
    print(f"The sum from {start} to {end} (parallel): {result_parallel}")
    print(f"Total workload time: {elapsed_time:.2f} seconds")
    print("Results are the same:", result_normal == result_parallel)
