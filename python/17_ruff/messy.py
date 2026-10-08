from collections import OrderedDict


def add(a, b):
    result = a + b
    return result


def check(x):
    if x is None:
        print("none!")
    return x


d = OrderedDict()
print(add(2, 3))
