from functools import reduce

# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1, 2, 3, 4]
copy_of_numbers = [x for x in numbers]
print(copy_of_numbers)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers1 = list(range(1, 11))
print(list(filter(lambda x: x % 2 == 0, numbers1)))
# Solve the task above using filter() with a lambda function.

# Given the list[("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
print("Sorted by number:", sorted(fruits, key=lambda x: x[1]))

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using reduce() and a lambda function.
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, numbers))

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
one_list = [num for sub in lists for num in sub]
print(one_list)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example{'a': 1, 'b': 2, 'c': 3} ->{1: 'a', 2: 'b', 3: 'c'}.
dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in dict.items()}
print(flipped_dict)
# flip back
dict = {value: key for key, value in flipped_dict.items()}
print(dict)
