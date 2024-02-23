from functools import reduce

# 1.Given a list of numbers, write a list comprehension that produces a copy of the list.
list_of_number = [2, 4, 6, 7, 56]
copy_list_of_number = [x for x in list_of_number]
print(f'A copy of the list - {copy_list_of_number}')

# 2.Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
number_list = range(1, 11)
even_numbers = [x for x in number_list if x % 2 == 0]
print(f'The even numbers - {even_numbers}')

# 3.Solve the task above using filter() with a lambda function.
new_list = list(filter(lambda x: x % 2 == 0, number_list))
print(f'The even numbers - {new_list}')

# 4.Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
given_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sort_by_number = sorted(given_list, key=lambda x: x[1])
print(f'Sorting list by the number - {sort_by_number}')

# 5.Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values
# using functools.reduce() from the standard library and a lambda function.
result = reduce(lambda x, y: x*y, [1, 2, 3, 4, 5])
print(f'The multiplication result - {result}')

# 6.Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension
# that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [x for y in list_of_lists for x in y]
print(f'Single list of all items - {single_list}')

# 7.Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dictionary = {'a': 1, 'b': 2, 'c': 3}
new_dictionary = {value: key for key, value in dictionary.items()}
print(f'Flipping dictionary -  {new_dictionary}')

