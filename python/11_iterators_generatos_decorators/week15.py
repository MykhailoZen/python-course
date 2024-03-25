import time

def time_to_run(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print("Calculation took", time.time() - start_time, "time to run")
    return wrapper

@time_to_run
def fibonacci(input):
    a = 0
    b = 1
    if input == 1:
        return b
    else:
        for i in range(1, input):
            c = a + b
            a = b
            b = c
        print(b)

fibonacci(99)

