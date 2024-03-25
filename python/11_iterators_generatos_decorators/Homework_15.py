import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        elapsed_time = time.monotonic() - start
        print(f"{func.__name__} took {elapsed_time:.3f} seconds.")
        return result

    return wrapper


@log_time
def test_function(n):
    return sum(range(n))


def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    test_function(1000000)
    for fib_number in fibonacci_generator(100):
        print(fib_number)
