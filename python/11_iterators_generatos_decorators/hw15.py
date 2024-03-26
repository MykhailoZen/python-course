#1.1 Create a decorator that logs the time taken by a function to execute.

import time
from datetime import datetime
from time import sleep

def logger(func):
    def wrapper(*args):
        start = time.time()
        print(f" {func.__name__} started at  {datetime.now()}")
        function = func(*args)
        end = time.time()
        ex_time = (end - start).__round__(3)
        print(f" {func.__name__} stopped at  {datetime.now()}")
        print(f" {func.__name__} execution time was {ex_time} seconds")
        return function
    return wrapper


@logger
def somefunc(sec):
    sleep(sec)
    pass

#example:
somefunc(3)


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

@logger
def fibogen(s_limit):
    a = 0
    b = 1
    while a <= s_limit:
        yield a
        a, b = b, a + b

#example
for num in fibogen(100):
    print(num)
    