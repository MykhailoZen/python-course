import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        """
        Logs the time taken by a function to execute
        :param args: any arguments
        :param kwargs: any other arguments
        :return: function duration
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f'Function {func.__name__} took: {duration:.3f} seconds for execution')
        return result

    return wrapper


def fibonacci(count: int):
    """
    Fibonacci sequence generator
    :param count: limit of numbers
    :return: generator of Fibonacci sequence
    """
    i, j = 0, 1
    for n in range(count):
        yield i
        i, j = j, i + j


for num in fibonacci(70):
    print(num)



