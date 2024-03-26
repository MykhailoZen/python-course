import time


# Create a decorator that logs the time taken by a function to execute.
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.15f} seconds to execute.")
        return result
    return wrapper

# Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Example usage:
@calculate_time
def fibonacci_numbers(limit):
    fib_sequence = list(fibonacci_generator(limit))
    return fib_sequence

# Generate Fibonacci numbers up to a specified limit using the generator function
# and log the time taken by a function to execute.
result = fibonacci_numbers(1000000)
print("Fibonacci Sequence:", result)