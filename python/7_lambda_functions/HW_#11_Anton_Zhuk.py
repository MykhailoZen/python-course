from functools import reduce

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Variant 1
copy_of_list_of_numbers_1 = list_of_numbers.copy()
print(f'Task 1. Variant 1. Result: {type(copy_of_list_of_numbers_1)} -> {copy_of_list_of_numbers_1}')
# Variant 2
copy_of_list_of_numbers_2 = [x for x in list_of_numbers]
print(f'Task 1. Variant 2. Result: {type(copy_of_list_of_numbers_2)} -> {copy_of_list_of_numbers_2}')

# 2. Given a list of numbers (e.g. range(1, 11)),
# write a list comprehension that produces a list of only the even numbers.
list_of_numbers_range = list(range(1, 11))
list_of_even_numbers = [x for x in list_of_numbers_range if x % 2 == 0]
print(f'Task 2. Result: {type(list_of_even_numbers)} -> {list_of_even_numbers}')

# 3. Solve the task above using filter() with a lambda function.
list_of_numbers_lambda = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(f'Task 3. Result: {type(list_of_numbers_lambda)} -> {list_of_numbers_lambda}')

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
list_with_fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
list_with_fruits.sort(key=lambda x: x[1])
print(f'Task 4. Result: {type(list_with_fruits)} -> {list_with_fruits}')

# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of
# all values using functools.reduce() from the standard library and a lambda function.
list_of_numbers_task_5 = [1, 2, 3, 4, 5]
calculate = reduce(lambda x, y: x * y, list_of_numbers_task_5)
print(f'Task 5. Result: {type(calculate)} -> {calculate}')

# Bonus practice (15 points for each):
# 6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list_of_all_items = [x for n in list_of_lists for x in n]
print(f'Task 6. Result: {type(single_list_of_all_items)} -> {single_list_of_all_items}')

# 7. Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dict_from_task = {'a': 1, 'b': 2, 'c': 3}
result = {x: y for y, x in dict_from_task.items()}
print(f'Task 7. Result: {type(result)} -> {result}')
