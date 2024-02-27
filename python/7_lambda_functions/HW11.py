from functools import reduce

# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1, 2, 3, 4, 5]
copy_list = numbers[:]
print("Copy of list:", copy_list)

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("List of even numbers:", even_numbers)

# Solve the task above using filter() with a lambda function.
even_numbers_filter = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print("Even numbers using filter:", even_numbers_filter)

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print("Sorted fruits:", sorted_fruits)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("Multiplication result:", result)

# Bonus Practice:

# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print("Flattened list:", flattened_list)

# Using a dict comprehension flip the dictionary (make keys from values and vice versa)
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}
print("Flipped dictionary:", flipped_dict)
