import time

def count_time_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting execution")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time)
        print("Finish execution")
    return wrapper


def fibonacci(num):
    fib_1, fib_2 = 1, 1
    yield fib_1
    if num > 1:
        yield fib_2
    for _ in range(2, num):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_2

fib = fibonacci(20)
for i in fib:
    print(i)

@count_time_decorator
def custom_sleep_function(num):
    print("Start sleeping")
    time.sleep(num)
    print("End sleeping")


custom_sleep_function(10)