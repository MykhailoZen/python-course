# Given a list of numbers, write a list comprehension that produces a copy of the list.
origin = [1, 2, 3, 4, 5]
copy = [num for num in origin]
print(origin)
print(copy)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even = [num for num in range(1, 11) if num%2==0]
print(even)
# Solve the task above using filter() with a lambda function.
even_by_lambda = filter(lambda n: n%2==0, range(1, 11))
print(list(even_by_lambda))

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("banana", 10), ("apple", 50), ("cherry", 30)]
fruits_sorted = sorted(fruits, key=lambda fruit: fruit[1])
print(fruits_sorted)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
from functools import reduce
list = [1, 2, 3, 4, 5]
result = reduce((lambda x, y: x * y), list)
print(result)

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_2 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
list_3 = [y for x in list_2 for y in x]
print(list_3)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dict = {'a': 1, 'b': 2, 'c': 3}
dict_swapped = {v: k for k, v in dict.items()}
print(dict_swapped)