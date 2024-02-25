# Practice (8 points for each):
#
# Given a list of numbers, write a list comprehension that produces a copy of the list.

import functools

given_list = ['1', '2', '2', '1']
new_list = [x for x in given_list]
print(new_list)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.

given_list = [x for x in range(1, 11)]
new_list = [x for x in given_list if x % 2 == 0]
print(new_list)

# Solve the task above using filter() with a lambda function.

given_list = [x for x in range(1, 11)]
even_only = lambda x: x % 2 == 0
new_list = list(filter(even_only, given_list))
print(new_list)

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.

given_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = list(sorted(given_list, key=lambda x: x[1]))
print(sorted_list)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.

given_list = [1, 2, 3, 4, 5]
multiplied = functools.reduce(lambda x, y: x*y, given_list)
print(multiplied)

# Bonus practice (15 points for each):
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list
# of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

given_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
result = [x for elem in given_list for x in elem]
print(result)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example:
# {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

given_dict = {'a': 1, 'b': 2, 'c': 3}
result = {v: k for (k, v) in given_dict.items()}
print(result)
