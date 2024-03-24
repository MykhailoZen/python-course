import time
from functools import reduce


# 1.1 Create a decorator that logs the time taken by a function to execute.


def log_time(func):
    """Decorator that logs the time taken by a function to execute."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} was run {end_time - start_time:.4f} in seconds.")
        return result

    return wrapper


# Example usage
@log_time
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


output = factorial(100000)

# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.


def fibonacci_generator(limit):
    a, b = 0, 1
    while True:
        if a > limit:
            break
        yield a
        a, b = b, a + b


# Example usage
print("Fibonacci numbers:")
for num in fibonacci_generator(365):
    print(num, end=" ")
