"""
Practice (8 points for each):
1. Given a list of numbers, write a list comprehension that produces a copy of the list.
2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
3. Solve the task above using filter() with a lambda function.
4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
"""
from functools import reduce
from itertools import chain
# Task:
# 1
primary_list = [1, 2, 3, 4, 5]
copy_list = [x for x in primary_list]
print(copy_list)
# 2
numbers = list(range(1, 11))
ev_numbers = [x for x in numbers if not x % 2]
print(ev_numbers)
# 3
f_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f_numbers)
# 4
fruit = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruit_s = sorted(fruit, key=lambda x: x[1])
print(fruit_s)
# 5
nums = [1, 2, 3, 4, 5]
list_m = (reduce(lambda x, y: x * y, nums))
print(list_m)

"""
Bonus practice (15 points for each):
--
1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), 
write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
--
2.Using a dict comprehension flip the dictionary (make keys from values and vice versa). 
For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
"""
#1
listed_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
# list comprehension
new_listed_list = [x for row in listed_lists for x in row]
print(new_listed_list)
# chain
other_listed_list = list(chain.from_iterable((listed_lists)))
print(other_listed_list)
#2
di: dict = {'a': 1, 'b': 2, 'c': 3}
# zip
di_new = dict(zip(di.values(), di.keys()))
print(di_new)
# comprehension
dict_inv = {value: key for key, value in di.items()}
print(dict_inv)