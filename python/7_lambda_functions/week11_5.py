#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using
# functools.reduce() from the standard library and a lambda function.

from functools import reduce

list_1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, list_1 )
print(result)


