
# 1. Practice - mandatory
#
# 1.1 Create a decorator that logs the time taken by a function to execute.

import  functools
import time

def timer_decorator(func):
    """Print the runtime of a decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function {func.__name__}() runs for {run_time:.4f} secs")
        return value

    return wrapper_timer

@timer_decorator
def waste_some_time(sec):
    time.sleep(sec)

waste_some_time(1)
waste_some_time(5)

# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

@timer_decorator
def fibonacci_generator(stop=20):
    """
       Generates Fibonacci numbers up to the specified limit of iterations.
       Parameters:
       - stop (int):
       The limit of iterations for generating Fibonacci numbers. Defaults to 20.
       - yield (int):
       The next Fibonacci number in the sequence.
       """
    current, next = 0, 1
    for i in range(0, stop):
        yield current
        current, next = next, current + next


f_sequence = fibonacci_generator(10)
print(type(f_sequence))
print(list(f_sequence))



