from functools import reduce

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
given_list = [1, 2, 3, 4, 5, 6, 7, 8]
copy = [num for num in given_list]
print(f" #1: {copy}")

# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
# assuming the range is optional I chose from 0 to 20
even = [num for num in range(21) if num % 2 == 0]
print(f" #2: {even}")

# 3. Solve the task above using filter() with a lambda function.
even_3 = list(filter(lambda num: (num % 2 == 0), range(21)))
print(f" #3: {even_3}")

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function
list_2 = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_2 = (sorted(list_2, key=lambda n: n[1]))
print(f" #4: {sorted_2}")

# 5. Given the list [1,2,3,4,5], calculate the multiplication result of all values using reduce() and a lambda function.
list_3 = [1, 2, 3, 4, 5]
reduced = (reduce(lambda x,y: x * y, list_3))
print(f" #5: {reduced}")

# Bonus # 1
#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [x for item in list_of_lists for x in item]
print(f" #B1: {single_list}")

# Bonus # 2
#Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dict_initial = {'a': 1, 'b': 2, 'c': 3}
flip = (dict([(fir, sec) for sec, fir in dict_initial.items()]))
print(f" #B2: {flip}")






