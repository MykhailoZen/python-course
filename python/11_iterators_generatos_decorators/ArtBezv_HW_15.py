#1.1 Create a decorator that logs the time taken by a function to execute.
import time

# Define the decorator
def time_execution(func):
    def cover(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)
        end_time = time.time()  # End time
        print(f"Time to execute the '{func.__name__}': {end_time - start_time:.2f} seconds")
        return result
    return cover

@time_execution
def test_function():
    print("Running example function...")
    time.sleep(3)

test_function()

#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

def fibonacci_number(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

limit = 100
fibonacci_sequence = fibonacci_number(limit)

for num in fibonacci_sequence:
    print(num)

