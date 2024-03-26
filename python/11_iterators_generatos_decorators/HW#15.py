import time


class CountDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{self.func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result


# function count something, then prints duration
@CountDecorator
def count_function():
    for i in range(1, 11):
        print(f"Counting: {i}")
        time.sleep(0.3)
    return "Done"


count_result = count_function()
print(count_result)


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 1, 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


# Function usage
limit = 100
fibonacci_func = FibonacciGenerator(limit)
fibonacci_sequence = list(fibonacci_func)
print(fibonacci_sequence)
