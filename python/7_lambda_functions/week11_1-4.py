#Practice (8 points for each):


#Given a list of numbers, write a list comprehension that produces a copy of the list.

list_1 = [1, 2, 3, 4, 5]


list_copy = [x for x in list_1]
#print(list_copy)

#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]

list_even = [y for y in list_2 if y % 2 != True]

#print(list_even)

#Solve the task above using filter() with a lambda function.

list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
list_lmb = list(filter(lambda z: (z % 2 == 0), list_3))
#print(list_lmb)


#Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.

list_4 = [("apple", 50), ("banana", 10), ("cherry", 30)]
list_srt = sorted(list_4, key = lambda a : a[1])
#print(list_srt)


#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
from functools import reduce

#Bonus practice (15 points for each):

#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
#Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.


