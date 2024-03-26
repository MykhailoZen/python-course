
#1.1 Create a decorator that logs the time taken by a function to execute.

import time

def execution_time(func):
    def wrapped():
        start_time = time.time()
        func()
        end_time = time.time()
        estimate = end_time - start_time
        print(estimate)
    return wrapped

@execution_time
def mult():
    print([i for i in range(1, 50000) if i % 2 == 0])

mult()


#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

def func(limit_number):
    a, b = 1, 1
    while a < limit_number:
        yield a
        a, b = b, a + b

print(list(func(15)))
