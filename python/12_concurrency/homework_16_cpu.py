import multiprocessing
import time

def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end+1))


def chunk_range(start: int, end: int, num_chunks: int) -> list:
    chunk_size = (end - start + 1) // num_chunks
    chunks = []
    for i in range(num_chunks):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if i < num_chunks - 1 else end
        chunks.append((chunk_start, chunk_end))
    return chunks


def calculate_sum_parallel(start: int, end: int, num_processes: int) -> int:
    chunks = chunk_range(start, end, num_processes)
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(calculate_sum, chunks)
    return sum(results)

if __name__ == "__main__":
    start_time = time.time()
    result_serial = calculate_sum(1, 2**30)
    serial_time = time.time() - start_time

    start_time = time.time()
    result_parallel = calculate_sum_parallel(1, 2**30, multiprocessing.cpu_count())
    parallel_time = time.time() - start_time

    print("Serial Result:", result_serial)
    print("Parallel Result:", result_parallel)
    print("Serial Time:", serial_time)
    print("Parallel Time:", parallel_time)

    # Verify the result:
    expected_result = 576460752840294400
    if result_serial == result_parallel == expected_result:
        print("Results verified!")
    else:
        print("Results verification failed!")
