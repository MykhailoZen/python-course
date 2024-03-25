import time
# 1.1 Create a decorator that logs the time taken by a function to execute.


def time_execution_decorator(func):
    def timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        execution_time = end - start
        execution_time_milliseconds = end - start * 1000
        milliseconds = int(execution_time_milliseconds % 1000)
        time_formatted = time.strftime('%H:%M:%S', time.gmtime(execution_time)) + f'.{milliseconds:03d}'

        print(f'Time taken for execution: {time_formatted}')
    return timer


# @time_execution_decorator
# def test_func():
#     print('Hello World!')
#
#
# test_func()


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

def fib_generator(limit):
    x, y = 0, 1

    while x < limit:
        yield x
        x, y = y, x + y


# for item in fib_generator(1025):
#     print(item)

