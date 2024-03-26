"""
1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
"""

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example
for number in fibonacci_generator(10):
    print(number)