import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} took {time.time() - start} seconds to execute.")
        return result

    return wrapper


@log_time
def test_function(n):
    return sum(range(n))


test_function(1000000)


def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


for fib_number in fibonacci_generator(100):
    print(fib_number)
