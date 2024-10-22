from functools import reduce

#Given a list of numbers, write a list comprehension that produces a copy of the list.
list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_0_1 = [i for i in list_0]
list_0_0 = [i for i in range(15)]
print(list_0_1)

#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
list_1 = [i for i in range(1, 11) if i%2 == 0]
print(list_1)

#Solve the task above using filter() with a lambda function.
list_1_2 = list(filter( lambda x: x%2 == 0, list_1))
print(list_1_2)

#Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
list_2 = [("apple", 50), ("banana", 10), ("cherry", 30)]
list_2.sort(key=lambda x: x[1])
print(list_2)

#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
list_3 = [1, 2, 3, 4, 5]
list_mult = reduce(lambda x, y: x * y, list_3)
print(list_mult)


#Bonus practice (15 points for each):
#Flattening: Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
new_list = [x for y in list_of_lists for x in y]
print(new_list)

#Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.'''
dicts = {'a': 1, 'b': 2, 'c': 3}
new_dict = {key: value for value, key in dicts.items()}
print(new_dict)







