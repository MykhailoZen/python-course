# 1.1 Create a decorator that logs the time taken by a function to execute.
import time

def time_calc(func): # decorator creatitng
    def wrapper(*args, **kwargs):
        print("Start function executing:")
        start = time.time()
        main_func = func (*args, **kwargs)
        end = time.time()
        finish_time = end - start
        print(f"Executing time of {func.__name__} is {finish_time} sec.")
        return main_func
    return wrapper

@time_calc # decorator executing
def cycle_in_cycle(): #some function for calculating cycle in cycle
    for j in range(1, 3500, 1):
        a = 0
        for i in range(j):
            a += (i**100)

cycle_in_cycle()

#1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.


def fibonacci_calc_generator(numbers_limit):
    x1, x2 = 0, 1 # first and second fibonacci numbers
    for n in range(numbers_limit):
        yield x1
        x1, x2 = x2, x1 + x2 #main fibonacci formula logic

#check
numbers_limit = 15
numb = fibonacci_calc_generator(numbers_limit)
print(f"Fibonnaci numbers of {numbers_limit}:")
for number in numb:
    print(number)



