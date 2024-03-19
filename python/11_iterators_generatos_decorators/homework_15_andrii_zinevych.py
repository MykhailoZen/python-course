# 1.1 Create a decorator that logs the time taken by a function to execute.
# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
# task 1.2 was example for task 1.1

import time


def logging_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function executed {execution_time:.10f} seconds.")
        return result
    return wrapper


@logging_time_decorator
def function_to_execution():
    def fibonacci(limit):
        a, b = 0, 1
        while a <= limit:
            yield a
            a, b = b, a + b

    fibonacci_gen = fibonacci(100)
    for num in fibonacci_gen:
        print(num)


function_to_execution()

# example of usage

"""
➜  python3 homework_15_andrii_zinevych.py
0
1
1
2
3
5
8
13
21
34
55
89
Function executed 0.0001180172 seconds.
"""