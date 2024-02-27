"""
Practice HW11

1. Given a list of numbers, write a list comprehension that produces a copy of the list.
2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
3. Solve the task above using filter() with a lambda function.
4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.

Extra:
6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
7. Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
"""

# Task1
numbers = [2, 5, 4, 8, 11]
numbers_duplicate = [n for n in numbers]
print("Task1 answer:")
print("List of numbers:", numbers)
print("Duplicated list of numbers:", numbers_duplicate)
print()

# Task2

init_list = range(0, 20)

even_numbers_list = [n for n in init_list if n % 2 == 0]
print("Task2 answer:")
print("Initial Number List:", list(init_list))
print("Even Number List:", even_numbers_list)
print()

# Task3

init_list = range(0, 20)

even_numbers = list(filter(lambda n: n % 2 == 0, init_list))
print("Task3 answer:")
print("Initial Number List:", list(init_list))
print("Even Number List:", even_numbers_list)
print()

# Task4

init_fruit_list = [("apple", 50), ("banana", 10), ("cherry", 30)]

sorted_list = sorted(init_fruit_list, key=lambda x: x[1])

print("Task4 answer:")
print("Initial Fruit List:", init_fruit_list)
print("Sorted Fruit List:", sorted_list)
print()

# Task5

from functools import reduce

print("Task5 answer:")
numb_list = [1, 2, 3, 4, 5]
res_of_multiplication = reduce(lambda x, y: x * y, numb_list)
print("Original List:", numb_list)
print("Multiplication Result:", res_of_multiplication)
print()
