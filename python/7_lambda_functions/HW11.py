# Practice
# 1.Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [5, 9, 12, 45, 78, 34, 99]
numbers_copy = [i for i in numbers]

# 2.Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces
#   a list of only the even numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [i for i in nums if i %2 == 0]

# 3.Solve the task above using filter() with a lambda function.
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums2 = list(filter(lambda x: x %2 == 0, nums2))

# 4.Given the list [("apple", 50), ("banana", 10), ("cherry", 30)],
#   sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])

# 5.Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values
#   using functools.reduce() from the standard library and a lambda function.

from functools import reduce
my_list = [1, 2, 3, 4, 5]
multiplication = reduce(lambda x,y: x*y, my_list)

# Bonus practice
# 1.Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),write a list comprehension that produces
#   a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
big_list = [i for row in list_of_lists for i in row]

# 2.Using a dict comprehension flip the dictionary (make keys from values and vice versa).
#   For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
my_dict = {'a': 1, 'b': 2, 'c': 3}
flip_dict = {value: key for key, value in my_dict.items()}