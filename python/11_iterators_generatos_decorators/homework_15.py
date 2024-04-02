from datetime import datetime
import time
from random import randint

# 1.1 Create a decorator that logs the time taken by a function to execute.
def decorator_function(original_fn):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = original_fn(*args, **kwargs)
        print(f"This time the function slept for: ", datetime.now() - start_time)
        return result
    return wrapper

@decorator_function
def sleep_function(a, b):
    print("This function will sleep for some time.")
    time.sleep(randint(a, b))

sleep_function(1, 5)

# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

def fibonacci_fn(number):
    a, b = 1, 1
    while a < number:
        yield a
        a, b = b, a + b

for n in fibonacci_fn(100):
    print(n)
