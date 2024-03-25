#1 Create a decorator that logs the time taken by a function to execute.
import time
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

# For ran:
@calculate_execution_time
def example_function():
    time.sleep(2)  # Simulate some processing time
    return "Done"

example_function()


#2 Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci_numbers(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# For ran:
fib_limit = 100
fib_gen = fibonacci_numbers(fib_limit)
print(list(fib_gen))
