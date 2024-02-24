import functools

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
def copy_of_list(list):
    return [x for x in list]

print(f"Task 1 - Result: {copy_of_list([1, 2, 3, 4, 65])}")

# 2. Given a list of numbers (e.g. range(1, 11)),
# write a list comprehension that produces a list of only the even numbers.

def even_nums(list):
    return [x for x in list if x % 2 == 0]

lst = [1,2,3,4,5,6,7,8,9,10,11]

print(f"Task 2 - Result: {even_nums(lst)}")


# 3. Solve the task above using filter() with a lambda function.
res_3 = list(filter(lambda x: (x % 2 == 0), lst))
print(f"Task 3 - Result: {res_3}")

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)],
# sort it by the number using the lambda function.
lst_4 = [("apple", 50), ("banana", 10), ("cherry", 30)]

res_4 = sorted(lst_4, key=lambda elem: elem[1], reverse=False)
print(f"Task 4 - Result: {res_4}")

# 5. Given the list [1, 2, 3, 4, 5],
# calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.
lst_5 = [1, 2, 3, 4, 5]

res_5 = functools.reduce(lambda x, y: x * y, lst_5)
print(f"Task 5 - Result: {res_5}")

# BONUS TASKS
# 6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
lst_6 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]

res_6 = [x for sublst in lst_6 for x in sublst]
print(f"Task 6 - Result: {res_6}")

# 7. Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dct_7 = {'a': 1, 'b': 2, 'c': 3}

res_7 = {value: key for key, value in dct_7.items()}
print(f"Task 7 - Result: {res_7}")
