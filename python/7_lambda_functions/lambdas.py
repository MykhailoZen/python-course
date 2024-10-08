from functools import reduce

#1. Given a list of numbers, write a list comprehension that produces a copy of the list.

list1 = [1,2,3]
copy=list1.copy()
print(copy)

#2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.

list2 = range(1, 11)
even = [number for number in list2 if number % 2 == 0]
print(even)

#3. Solve the task above using filter() with a lambda function.

even3 = list(filter(lambda x: x % 2 == 0, list2))
print(even3)

#4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.

list4 = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted = sorted(list4, key=lambda x: x[1])
print(sorted)

#5 Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.

list5 = [1, 2, 3, 4, 5]
multiplied = reduce(lambda x, y: x * y, list5)
print(multiplied)

#6 Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

list6 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
cumulated = [number for temp_list in list6 for number in temp_list]
print(cumulated)

#7 Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)