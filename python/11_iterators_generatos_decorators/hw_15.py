"""

1. Practice - mandatory

1.1 Create a decorator that logs the time taken by a function to execute.

1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

"""
#1

print()
print("it's working, no worries, just wait a bit")
print()

import time

def time_spent(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken by '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example of usage:
@time_spent
def delay_func():
    # Simulation of 5 sec delay
    time.sleep(5)
    print("Function execution has been ended")

delay_func()

#2

def fibonacci_generator(limit):
    # Variables for 2 first numbers of F-ci sequence
    a, b = 0, 1

    # Specify limit for Fibonacci generator
    while a <= limit:
        yield a
        a, b = b, a + b


# Example of usage:
limit = 70
fibonacci_sequence = list(fibonacci_generator(limit))

print("Fibonacci numbers up to", limit, ":")
print(fibonacci_sequence)
