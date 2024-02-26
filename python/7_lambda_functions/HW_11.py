# Practice:
# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.

nums = [34, 456, 67, 34, 6, 789, 45, 131, 56]
nums_copy = [x for x in nums]
print("Copy of the list:", nums_copy)

# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.

nums_even = [x for x in range(1, 11) if x % 2 == 0]
print("List of only the even numbers:", nums_even)

# 3. Solve the task above using filter() with a lambda function.

numbers = range(1, 11)
print("List of only the even numbers:", list(filter(lambda y: y % 2 == 0, numbers)))

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.

fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
print("Sorted by the number:",
      sorted(fruits, key=lambda x: x[1]))

# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
from functools import reduce

list = [1, 2, 3, 4, 5]
print("Multiplication result of all values:", reduce(lambda x, y: x * y, list))

# Bonus practice:
# 1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
print("Single list of all items:", [a for b in lists for a in b])

# 2. Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

dict = {'a': 1, 'b': 2, 'c': 3}
print("Keys from values and vice versa:", {value: key for key, value in dict.items()})