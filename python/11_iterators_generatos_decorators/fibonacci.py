import time
from functools import wraps


def time_taken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by '{func.__name__}': {end_time - start_time} seconds")
        return result

    return wrapper


# Example usage
@time_taken
def example_function():
    time.sleep(2)
    print("Function executed.")


example_function()


def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# Example usage:

fib = fibonacci_generator(100)
for num in fib:
    print(num)
