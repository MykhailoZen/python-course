# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.


import time


def time_taken(func):
    """
    This code defines a decorator time_taken that
    measures the time taken by a function that generates Fibonacci
    numbers up to a specified limit to execute.
    """
    def wrapped(*args):
        start_time = time.monotonic()
        result = func(*args)
        end_time = time.monotonic()
        return result, end_time - start_time
    return wrapped


@time_taken
def fibonacci_numbers_generator(x):
    a, b = 0, 1
    while True:
        yield a
        if a >= x:
            break
        a, b = b, a + b


x = 603628
fib_nums_gen, execution_time = fibonacci_numbers_generator(x)
# print(fib_nums_gen) to make sure it's a generator
for num in fib_nums_gen:
    print(num)

print(f"It took {execution_time:.6f} seconds to execute fibonacci_numbers function")

