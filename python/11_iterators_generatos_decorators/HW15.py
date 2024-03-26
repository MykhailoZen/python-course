# 1. Create a decorator that logs the time taken by a function to execute.

import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} execution time: {execution_time:.4f} ")
        return result
    return wrapper


# 2. Write a generator function that generates Fibonacci numbers up to a specified limit

# Variant 1
def fibonacci_generator(n):
    x, y = 0, 1
    while x <= n:
        yield x
        x, y = y, x + y


for i in fibonacci_generator(10):
    print(i)

# Variant 2
def fibonacci_generator():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


for i in fibonacci_generator():
    if i in range(10):
        print(i)

