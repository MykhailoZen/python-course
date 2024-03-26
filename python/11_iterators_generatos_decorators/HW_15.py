# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
import time


def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


limit = 33
fibonacci_numbers = []
for number in fibonacci_generator(limit):
    fibonacci_numbers.append(number)
print(fibonacci_numbers)


# 1.1 Create a decorator that logs the time taken by a function to execute.

def time_execution_decorator(even_numbers):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Starting execution")
        even_numbers(*args, **kwargs)
        end_time = time.time()
        print("Stop execution")

        execution_time = end_time - start_time

        return execution_time

    return wrapper

@time_execution_decorator
def even_numbers(all_numbers):
    return [x for x in all_numbers if x % 2 == 0]

all_numbers = range(20, 99999999)
even_nums = even_numbers(all_numbers)
execution_time = even_nums
print(f"Time for execution {execution_time:.2f} seconds")

