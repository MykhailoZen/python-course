# Given a list of numbers, write a list comprehension that produces a copy of the list.
original_list = [1, 2, 3, 4, 5]
copied_list = [number for number in original_list]


# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers = range(1, 11)
even_numbers = [num for num in numbers if num % 2 == 0]


# Solve the task above using filter() with a lambda function.
numbers = range(1, 11)
even_numbers_2 = list(filter(lambda x: x % 2 == 0, numbers))


# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])


# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the
# standard library and a lambda function.
import functools
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
