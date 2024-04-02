import time
from multiprocessing import Pool
from functools import wraps


def measure_time(func):
    """The function can measure time taken by a function to execute"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_to_return = func(*args, **kwargs)
        end_time = time.time()
        time_for_execution = end_time - start_time
        print(f"Time spent for function {func.__name__}: {time_for_execution:.4f} seconds")
        return function_to_return
    return wrapper


@measure_time
def calculate_sum(start, end):
    """Function calculates sum of the given range of numbers"""
    result = 0
    for number in range(start, end+1):
        result += number
    return result


@measure_time
def calculate_multiple_cpu(start, end):
    """Function executes another function in parallel on the specified amount of CPUs"""
    chunk_size = (end - start + 1) // cpu_count
    ranges = [(start + i * chunk_size, start + (i + 1) * chunk_size - 1) for i in range(cpu_count)]
    with Pool(processes=cpu_count) as pool:
        results = pool.starmap(calculate_sum, ranges)
    return sum(results)


if __name__ == "__main__":
    cpu_count = 32
    start_range = 1
    end_range = 2 ** 30
    print(calculate_sum(start_range, end_range))
    print(calculate_multiple_cpu(start_range, end_range))
