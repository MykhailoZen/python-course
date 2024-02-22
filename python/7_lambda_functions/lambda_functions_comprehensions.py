import functools

# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers_list1 = [1, 2, 3, 4, 5]
copied_numbers_list = [num for num in numbers_list1]

print(copied_numbers_list)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
new_list = [num for num in numbers_list2 if num % 2 == 0]

print(new_list)

# Solve the task above using filter() with a lambda function
numbers_list3 = list(range(1, 11))
new_list1 = list(filter(lambda num: num % 2 == 0, numbers_list3))

print(new_list1)

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruits.sort(key=lambda x: x[1])

print(fruits)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using reduce() and a lambda function.
numbers_list4 = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x * y, numbers_list4))

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]).
# Write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]
numbers_list5 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
new_list5 = [y for x in numbers_list5 for y in x]

print(new_list5)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dictionary1 = {'a': 1, 'b': 2, 'c': 3}
swap_dict1 = {v: k for k, v in dictionary1.items()}

print(swap_dict1)