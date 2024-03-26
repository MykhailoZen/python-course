import time

# 1.1 Create a decorator that logs the time taken by a function to execute.
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Function {func.__name__} executed in {execution_time}')
        return result
    return wrapper


@log_execution_time
def example_func():
    time.sleep(5)
    print('example_func executed')


example_func()


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))
