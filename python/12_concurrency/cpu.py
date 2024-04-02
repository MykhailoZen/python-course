from concurrent.futures import ProcessPoolExecutor
import time
import os
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] duration is {end - start:.1f} seconds")
        return result

    return wrapper


@time_decorator
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))


def generate_chunks(start, end, num_chunks):
    total_size = end - start + 1
    chunk_size = max(total_size // num_chunks, 1)  # min 1
    chunks = []
    for i in range(start, end + 1, chunk_size):
        chunk_start = i
        chunk_end = min(i + chunk_size - 1, end)
        chunks.append((chunk_start, chunk_end))
    return chunks


@time_decorator
def calculate_sum_parallel(start, end, num_chunks):
    chunks = generate_chunks(start, end, num_chunks)
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(calculate_sum, chunk_start, chunk_end) for chunk_start, chunk_end in chunks]
        total_sum = sum(future.result() for future in futures)
    return total_sum


if __name__ == '__main__':
    start_index = 1
    end_index = 2 ** 30
    workers = 4

    print("=====================")
    print("=== calculate_sum ===")
    print("=====================")
    print(calculate_sum(start_index, end_index))
    print()

    print("==============================")
    print("=== calculate_sum_parallel ===")
    print("==============================")
    print(calculate_sum_parallel(start_index, end_index, workers))
