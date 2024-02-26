import functools

# Given a list of numbers, write a list comprehension that produces a copy of the list.
list_of_numbers = [10, 20, 30]
copied_list = [x for x in list_of_numbers]
print("Copied list:", copied_list)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a
# list of only the even numbers.
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print("Even numbers: ", even_numbers)

# Solve the task above using filter() with a lambda function.
even_numbers_with_filter = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print("Even numbers using filter(): ", even_numbers_with_filter)

# Given the list [("apple", 50), ("banana", 10),
# ("cherry", 30)], sort it by the number using the lambda function
list_to_sort = [("apple", 50), ("banana", 10), ("cherry", 30)]
list_to_sort.sort(key=lambda x: x[1])
print("Sorted list: ", list_to_sort)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.
given_list = [1, 2, 3, 4, 5]
print("Multiplication result: ", functools.reduce(lambda a, b: a*b, given_list))

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a
# single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [x for y in list_of_lists for x in y]
print("Single list :", single_list)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dict_to_flip = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in dict_to_flip.items()}
print("Flipped dict: ", flipped_dict)
