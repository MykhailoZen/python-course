from functools import reduce

'''
1 - Given a list of numbers, write a list comprehension that produces a copy of the list
'''
list_n1 = [1, 2, 3, 4, 5]
list_n1_copy = [x for x in list_n1]
print(f"#1 === {list_n1_copy}")

'''
2 - Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only
the even numbers
'''
list_n2 = range(1, 11)
list_n2_even = [x for x in list_n2 if x % 2 == 0]
print(f"#2 === {list_n2_even}")

'''
3 - Solve the task above using filter() with a lambda function
'''
list_n3 = range(1, 11)
list_n3_filtered = list(filter(lambda x: x % 2 == 0, list_n3))
print(f"#3 === {list_n3_filtered}")

'''
4 - Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function
'''
list_n4 = [("apple", 50), ("banana", 10), ("cherry", 30)]
list_n4_sorted = sorted(list_n4, key=lambda x: x[1])
print(f"#4 === {list_n4_sorted}")

'''
5 - Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
from the standard library and a lambda function
'''
list_n5 = [1, 2, 3, 4, 5]
list_n5_reduced = reduce(lambda x, y: x * y, list_n5)
print(f"#5 === {list_n5_reduced}")

'''
6 - Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces
a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4])
'''
list_n6 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
list_n6_single = [x for list_mini in list_n6 for x in list_mini]
print(f"#6 === {list_n6_single}")

'''
7 - Using a dict comprehension flip the dictionary (make keys from values and vice versa).
For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}
'''
list_n7 = {'a': 1, 'b': 2, 'c': 3}
list_n7_flip = {value: key for key, value in list_n7.items()}
print(f"#7 === {list_n7_flip}")
