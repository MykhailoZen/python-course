#1. Create a decorator that logs the time taken by a function to execute.

import time

def time_logger(func):
    start=time.time()
    result=func()
    end=time.time()
    print("Performing function took", "{:.2e}".format(end-start)," seconds")
    return result

@time_logger
def some_func():
    result = 1
    number=100
    for number in range(1,number+1):
        result = result*number
    time.sleep(0.003)
    print("{:.2e}".format(result))

#2. Write a generator function that generates Fibonacci numbers up to a specified limit.

def fibonacci(number):
    a,b=1,0
    while b<=number:
        a,b=b,a+b
        yield a

fib=fibonacci(1000)
for num in fib:
    print(num)


