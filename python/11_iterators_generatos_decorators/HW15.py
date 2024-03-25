from itertools import islice
from time import perf_counter
from math import factorial

# Create a decorator that logs the time taken by a function to execute.
def timer(function):
    def wrapper(args):
        timer_start = perf_counter()
        function(args)
        timer_end = perf_counter()
        timer_execution = timer_end - timer_start
        return f"The execution time of {function.__name__} is {timer_execution} seconds."
    return wrapper


@timer
def random_factorial(n):
    res = []
    for i in range(n):
        res.append(factorial(i))
    return res


final_result = random_factorial(10)


# Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci():
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current


f = iter(list(islice(fibonacci(), 0, 15)))

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

