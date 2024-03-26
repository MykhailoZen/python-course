import time
from functools import wraps

# Decorator to log the time taken by a function to execute
def calculate_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# Generator function to generate Fibonacci numbers up to a specified limit
@calculate_time
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example usage
limit = 1000
for num in fibonacci_generator(limit):
    print(num)
