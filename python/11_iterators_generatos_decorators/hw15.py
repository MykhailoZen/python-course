#Create a decorator that logs the time taken by a function to execute.
import time

def log_time_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: '{func.__name__}': {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@log_time_dec
def multiply(a, b):
    time.sleep(1)  # Simulating some time-consuming operation
    return a * b

print(multiply(3, 5))

#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
def generate_fibonacci_numbers(limit):
    current, next_num = 0, 1
    while current < limit:
        yield current
        current, next_num = next_num, current + next_num

limit = 50
fibonacci_numbers = list(generate_fibonacci_numbers(limit))
print(f"Fibonacci numbers up to {limit}: {fibonacci_numbers}")
