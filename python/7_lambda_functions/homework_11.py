from functools import reduce

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
my_list = [1, 5, 8, 10]

new_list = [num for num in my_list]

print(new_list)


# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces
# a list of only the even numbers.
another_list = list(range(1, 11))

even_list = [number for number in another_list if number % 2 ==0]

print(even_list)


# 3. Solve the task above using filter() with a lambda function.

filtered_list = list(filter(lambda x: x % 2 == 0, list(range(1, 11))))

print("Filtered list:", filtered_list)


# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.

fruit_list = [("apple", 50), ("banana", 10), ("cherry", 30)]

sorted_fruits = sorted(fruit_list, key=lambda x: x[1])

print("Sorted fruits list:", sorted_fruits)


# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.

result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

print("Multiplied list value:", result)

# Bonus practice 1.
# Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension
# that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

great_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]

result_list = [elem for sublist in great_list for elem in sublist]

print("Bonus practice 1 result:", result_list)


# Bonus practice 2.
# Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.

my_dict = {'a': 1,
           'b': 2,
           'c': 3}

changed_dict = {value: key for key, value in my_dict.items()}
print(my_dict.items())

print("Bonus practice 2 result:", changed_dict)