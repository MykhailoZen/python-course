#1.1 Create a decorator that logs the time taken by a function to execute.

import time

def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

# Example usage:
@timeit_decorator
def example_function(n):
    # Some time-consuming operation
    total = 0
    for i in range(n):
        total += i
    return total

result = example_function(100)
print("Result:", result)


#Fibonacci number using memorizer
'''
#Fibonacci number using memorizer

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

print(fibonacci(8))
'''

# decorator function that generates Fibonacci numbers up to a specified limit.

'''
def fibon(func):
    def wrapper(limit):
        result = func(limit)  # Call the original function with the provided argument
        return result  # Return the result of the original function
    return wrapper

@fibon
def fibonacci_generator(limit):
    a, b = 0, 1
    fib_sequence = []
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

result = fibonacci_generator(100)  # Example limit, adjust as needed
print("Result:", result)
'''

#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Usage:
for num in fibonacci_generator(220):  # Adjust the limit as needed
    print(num)

