"""
1.1 Create a decorator that logs the time taken by a function to execute.
1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
"""
import timeit
from random import random
import time

#1.1
def timed(inner_func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        inner_func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f'it takes {duration} secs to execute')
    return wrapped_func

def text(inner_func):
    def wrapped_func(*args, **kwargs):
        print('The execution is started')
        inner_func(*args, **kwargs)
        print('The execution is ended. No fails')
    return wrapped_func

@timed
def function(x=10):
    for i in range(0, 10000):
        x += random()
    return x


@timed
def another_function(x = 55):
    for i in range(100, 10000000):
        x -= 45
    return x

@text
@timed
def do_something(n):
    for x in range(n):
        for y in range(n):
            return x * y


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

@timed
def print_fibonacci(n):
    result = fibonacci(n)
    print(f'fibonacci num is {result}')

function(5)
do_something(5)
print_fibonacci(10)

#2.2
def fibonacci_generator(stop):
    current_fib = 0
    next_fib = 1
    for x in range(0, stop):
        fib_num = current_fib
        current_fib, next_fib = (next_fib, current_fib + next_fib)
        yield fib_num


print(f'This is fibonacci sequence: {(list(fibonacci_generator(5)))}')

for value in fibonacci_generator(5):
    print(value)


sum_fib = sum(fibonacci_generator(10))
print(sum_fib)



