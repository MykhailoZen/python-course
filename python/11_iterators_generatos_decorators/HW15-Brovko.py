# 1.1 Create a decorator that logs the time taken by a function to execute.
import time


def time_taken(func):
    def wrapper(*args, **kwargs):
        started = time.time()
        func(*args, **kwargs)
        result = time.time() - started
        print (f"Your function ({func.__name__}) took {result} second(s) to execute")
        return result
    return wrapper


@time_taken
def waste_time(seconds):
    time.sleep(seconds)


def fibonate(num):
    a, b = 0, 1
    for i in range(num+1):
        yield a
        a, b = b, a + b


def main():
    pass

waste_time(2)
fib_sequence = list(fibonate(5))
print(fib_sequence)


if __name__ == '__main__':
    main()
