import time


# 1.1 Create a decorator that logs the time taken by a function to execute.
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        print(f"Function {func.__name__} executed in {exec_time:}")

        return result

    return wrapper


@timer
def example(sec):
    time.sleep(sec)


example(1)
example(5)
example(9)


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

@timer
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(f'Result: {list(fib(10))}')
