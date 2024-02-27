
#1.Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers_list_1 = [2, 4, 93, 63, 99, 1, 15]
print([numbers_list_1 for i in range(1)])


#2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
print([i for i in range(1, 11) if i % 2 == 0])


#3. Solve the task above using filter() with a lambda function.
numbers_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(filter(lambda a: a % 2 == 0, numbers_list_2)))


#4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
numbers_list_3 = [("apple", 50), ("banana", 10), ("cherry", 30)]
print(sorted(numbers_list_3, key=lambda a: a[1]))


#5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
from functools import reduce
numbers_list_4 = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, numbers_list_4))


#Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print({value: key for key, value in my_dict.items()})
