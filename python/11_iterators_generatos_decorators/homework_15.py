import time
from functools import wraps


def measure_time(func):
    """The function can measure time taken by a function to execute"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_to_return = func(*args, **kwargs)
        end_time = time.time()
        time_for_execution = end_time - start_time
        print(f"Time spent for function {func.__name__}: {time_for_execution:.4f} seconds")
        return function_to_return
    return wrapper


@measure_time
def test_function():
    for sec in range(3, 0, -1):
        print(f"Waiting {sec} seconds...")
        time.sleep(1)
    return "End of execution"


def fibonacci(number):
    """The function generates fibonacci numbers"""
    x, y = 0, 1
    count = 0
    while count < number:
        yield x
        x, y = y, x + y
        count += 1


print(test_function())
numbers = fibonacci(10)
for i in numbers:
    print(i)
