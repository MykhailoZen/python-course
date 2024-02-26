from functools import reduce

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [5, 1, 5, 1, 5]
copy_list = [x for x in numbers]
print("1.Copy list:", copy_list)

# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers = range(1, 11)
only_even_numbers = [x for x in numbers if x % 2 == 0]
print("2.Only even numbers:", only_even_numbers)

# 3. Solve the task above using filter() with a lambda function.
only_even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("3.Only even numbers using filter():", only_even_numbers)

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print("4.Sorted fruits using lf:", sorted_fruits)

# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
numbers = [1, 2, 3, 4, 5]
calculate_result = reduce(lambda x, y: x * y, numbers)
print("5.Calculate_result:", calculate_result)

# 1b. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
# List comprehension to produce a single list of all items from a list of lists:

lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
comprehension_list = [item for sublist in lists for item in sublist]
print("1.b Comprehension list:", comprehension_list)

# 2b. Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
example_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
flipped_dict = {value: key for key, value in example_dict.items()}
print("2.b Flipped dictionary:", flipped_dict)