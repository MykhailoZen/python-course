#1.1 Create a decorator that logs the time taken by a function to execute.
import time
def logger(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print("start:", t1)
        result = func(*args, **kwargs)
        t2 = time.time()
        print("finish:", t2)
        print(f"Delta T = {t1 - t2}")
        return result
    return wrapper
def sleep(n):
    time.sleep(n)
    print("wake up after sleeping")
check = logger(sleep)
check(3)

#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci_gen(limit, a=0, b=1):
    if a <= limit:
        yield a
        yield from fibonacci_gen(limit,b, a + b)

limit = 200
fib_numbers = list(fibonacci_gen(limit))
print("Fibonacci numbers list with limit 200:", fib_numbers)