import logging
import time
from concurrent.futures import ProcessPoolExecutor
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("cpu.log", mode="w"),
    ],
)

logging.getLogger().handlers[1].setLevel(logging.INFO)  # File


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.debug(f"[{func.__name__}] duration is {end - start:.1f} s")
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
        futures = [
            executor.submit(calculate_sum, chunk_start, chunk_end)
            for chunk_start, chunk_end in chunks
        ]
        total_sum = sum(future.result() for future in futures)
    return total_sum


if __name__ == "__main__":
    start_index = 1
    end_index = 2**30
    workers = 32

    logging.info(
        f"[calculate_sum] - " f"{calculate_sum(start_index, end_index)}"
    )
    logging.info(
        f"[calculate_sum_parallel] - "
        f"{calculate_sum_parallel(start_index, end_index, workers)}"
    )
