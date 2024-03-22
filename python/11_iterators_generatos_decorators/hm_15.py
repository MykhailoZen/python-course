import functools
import time
from typing import Union


# 1.1 Create a decorator that logs the time taken by a function to execute.
def time_it(func):
    """
    :param func: function
    :return: the time taken by a function to execute
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time} seconds to execute.")
        return result
    return wrapper


@time_it
def my_function(seconds: Union[int, float]):
    """
    :param seconds: seconds
    """
    time.sleep(seconds)


# 1.2 Write a generator function that generates Fibonacci numbers up to a specified limit.
def fibonacci_generator(stop: int):
    """
    :param stop: number for Fibonacci sequence
    :return: Fibonacci numbers
    """
    try:
        current_num_fib = 0
        next_num_fib = 1
        if stop < 0:
            for item in range(stop, 0):
                fib_number = current_num_fib
                current_num_fib, next_num_fib = (
                    next_num_fib, current_num_fib - next_num_fib
                )
                yield fib_number
        else:
            for item in range(0, stop):
                fib_number = current_num_fib
                current_num_fib, next_num_fib = (
                    next_num_fib, current_num_fib + next_num_fib
                )
                yield fib_number
    except TypeError as type_er:
        print(f'Please use integer. {type_er}')


def print_list_from_generator(list_of_date):
    """
    :param list_of_date: list of data from generator
    :return: list from generator one by one
    """
    try:
        new_list_of_date = iter(list_of_date)
        while True:
            print(next(new_list_of_date))
    except StopIteration:
        print(f'End of iterator reached')


if __name__ == "__main__":
    # Verification a decorator that logs the time taken by a function to execute
    my_function(5.9)

    # Verification type error in fibonacci_generator
    list_of_fibonacci = list(fibonacci_generator('uihu'))
    # Verification negative number
    num = -8
    list_of_fibonacci1 = list(fibonacci_generator(num))[::-1]
    print(f'Fibonacci sequence for {num}: {list_of_fibonacci1}')
    # Verification positive number
    num2 = 5
    list_of_fibonacci2 = list(fibonacci_generator(num2))
    print(f'Fibonacci sequence for {num2}: {list_of_fibonacci2}')
    # Iterating through the iterator
    print_list_from_generator(list_of_fibonacci2)
    