import functools


# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1, 5, 76, 4, 3, 14]
l1 = [x for x in numbers]

# 2. Given a list of numbers (e.g. range(1, 11)),
# write a list comprehension that produces a list of only the even numbers.
l2 = [x for x in range(1, 11) if x % 2 == 0]

# 3. Solve the task above using filter() with a lambda function.
l3 = list(filter(lambda x: x % 2 == 0, range(1, 11)))

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruits.sort(key=lambda fruit: fruit[1])

# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values
# using functools.reduce() from the standard library and a lambda function.
multiplication_list = [1, 2, 3, 4, 5]
result = functools.reduce(
    lambda acc, multiplicator: acc * multiplicator, multiplication_list, 1
)


# Bonus practice (15 points for each):
# 1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4])
lol = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
l4 = [x for y in lol for x in y]

# 2. Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}
d = {"a": 1, "b": 2, "c": 3}
d2 = {a: b for b, a in d.items()}
