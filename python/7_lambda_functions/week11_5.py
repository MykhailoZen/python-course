#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using
# functools.reduce() from the standard library and a lambda function.

from functools import reduce

def multiply_num(a, b):
    res_mul = a * b
    return res_mul

list_1 = [1, 2, 3, 4, 5]
result = reduce(multiply_num, list_1)
print(result)

