"""
1.1 Create a decorator that logs the time taken by a function to execute.
"""
import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} sec")
        return result
    return wrapper

# Example
@time_logger
def example_function():
    time.sleep(1)
    print("Function completed.")

example_function()
