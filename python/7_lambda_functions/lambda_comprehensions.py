from functools import reduce

# Task 1
# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers_t1 = [1, 2, 3, 4, 5, 6, 7]
copy_of_numbers = [x for x in numbers_t1]

print(copy_of_numbers)

# Task 2
# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers_t2 = range(1, 11)
even_numbers_t2 = [x for x in numbers_t2 if x % 2 == 0]

print(even_numbers_t2)

# Task 3
# Solve the task above using filter() with a lambda function.
numbers_t3 = range(1, 11)
even_numbers_t3 = list(filter(lambda x: x % 2 == 0, numbers_t3))

print(even_numbers_t3)

# Task 4
# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])

print(sorted_fruits)

# Task 5
# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.
numbers_t4 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers_t4)

print(result)

# Task 6
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list
# of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [item for sublist in list_of_lists for item in sublist]

print(single_list)

# Task 7
# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
key_value_dict = {'a': 1, 'b': 2, 'c': 3}
value_key_dict = {value: key for key, value in key_value_dict.items()}

print(value_key_dict)
