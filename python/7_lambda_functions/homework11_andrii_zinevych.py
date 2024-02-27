import functools
from functools import reduce

print('1. Given a list of numbers, write a list comprehension that produces a copy of the list.')

list_of_numbers = [1, 2, 3, 4, 5]
copied_list = list_of_numbers.copy()
print(copied_list)

print('2. Given a list of numbers (e.g. range(1, 11)), '
      'write a list comprehension that produces a list of only the even numbers.')

list_of_numbers = range(1, 11)
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
print(even_numbers)

print('3. Solve the task above using filter() with a lambda function.')

task = range(1, 11)
even_numbers = list(filter(lambda x: x % 2 == 0, task))
print(even_numbers)

print('4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], '
      'sort it by the number using the lambda function.')


list_base = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(list_base, key=lambda x: x[1])
print(sorted_list)

print('5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values '
      'using functools.reduce() from the standard library and a lambda function.')

list_base = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x * y, list_base)
print(result)

print('6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), '
      'write a list comprehension that produces a single list of all items '
      '(e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).')

list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = reduce(lambda x, y: x + y, list_of_lists)
print(single_list)

print("7. Using a dict comprehension flip the dictionary (make keys from values and vice versa). "
      "For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.")

dict_base = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in dict_base.items()}
print(flipped_dict)
