# Given a list of numbers, write a list comprehension that produces a copy of the list.
import functools

numbers_1 = [2, 5, 7, 8, 9, 13]
numbers_2 = [x for x in numbers_1]

print(numbers_2)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
all_numbers = range(1, 11)
even_numbers = [x for x in all_numbers if x % 2 == 0]

print(even_numbers)

# Solve the task above using filter() with a lambda function.
even_numbers_1 = list(filter(lambda x: x % 2 == 0, all_numbers))
print(even_numbers_1)

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruits.sort(key=lambda x: x[1])
print(fruits)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.
num_list = [1, 2, 3, 4, 5]

multiplication_result = functools.reduce(lambda x, y: x * y, num_list)
print(multiplication_result)

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single
# list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

num_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
all_list = [x for y in num_lists for x in y]
print(all_list)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1,
# 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
my_dict = {'a': 1, 'b': 2, 'c': 3}
flip_dict = {k: v for v, k in my_dict.items()}
print(flip_dict)

