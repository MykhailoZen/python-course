"""First task"""
list_n = [1, 2, 3]
copy = [x for x in list_n]
print(copy)

"""Second task"""
numbers = range(1, 11)
even_numb = [numb for numb in numbers if numb % 2 == 0]
print(even_numb)

"""Third task"""
numbers = range(1, 11)
even_numb = list(filter(lambda numb: numb % 2 == 0, numbers))
print(even_numb)

"""Fourth task"""
name_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = list(sorted(name_list, key=lambda num: num[1]))
print(sorted_list)

"""Fifth task"""
import functools

numbers = [1, 2, 3, 4, 5]
calculate = functools.reduce(lambda x, y: x * y, numbers)
print(calculate)
