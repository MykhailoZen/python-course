print("Practice:")
from functools import reduce


# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
numb_list = [12, 23, 34, 45, 55]
copy_list = [x for x in numb_list]
print("1. Original list:", numb_list)
print("1. Copy of the list:", copy_list)


# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("2. Even numbers: ", even_numbers)


# 3. Solve the task above using filter() with a lambda function.
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print("3. Even numbers via lambda: ", even_numbers)


# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
lst = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print("4. Sorted list: ", sorted_lst)


# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print("5. Multiplication: ", result)

# Bonus practice:
print("Bonus practice:")
# 1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [item for sublist in list_of_lists for item in sublist]
print("1. Single list: ", single_list)


# 2. Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}
print("2. Flipped dictionary: ",flipped_dict)