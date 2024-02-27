# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers_list = [1, 2, 3, 4, 5]
copied_list = [x for x in numbers_list]
print(copied_list)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers_list = range(1, 11)
even_numbers = [x for x in numbers_list if x % 2 == 0]
print(even_numbers)

# Solve the task above using filter() with a lambda function.
numbers_list = range(1, 11)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print(even_numbers)

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(fruits_list, key=lambda x: x[1])
print(sorted_list)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

# Bonus:
lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
flattened_list = [item for sublist in lists for item in sublist]
print(flattened_list)

# bonus2:
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}
print(flipped_dict)
