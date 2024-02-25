import functools

"""   
    Task 1 
    Conditions: given a list of numbers 
    To Do: write a list comprehension that produces a copy of the list.
"""

def copy_of_list(lst_1):
    return [x for x in lst_1]


print(f"Task 1 - Result: {copy_of_list([1, 2, 3, 4, 65])}")

""" 
    Task 2
    Conditions: given a list of numbers (e.g. range(1, 11))
    To Do: write a list comprehension that produces a list of only the even numbers.
"""

def even_nums(lst_2):
    return [x for x in lst_2 if x % 2 == 0]


print(f"Task 2 - Result: {even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])}")

""" 
    Task 3
    To Do: Solve the task above using filter() with a lambda function.
"""
res_3 = list(filter(lambda x: (x % 2 == 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(f"Task 3 - Result: {res_3}")

"""
    Task 4
    Condition: given the list [("apple", 50), ("banana", 10), ("cherry", 30)],
    To Do:sort it by the number using the lambda function.
"""
lst_4 = [("apple", 50), ("banana", 10), ("cherry", 30)]

res_4 = sorted(lst_4, key=lambda elem: elem[1], reverse=False)
print(f"Task 4 - Result: {res_4}")

"""
    Task 5 
    Condition: given the list [1, 2, 3, 4, 5]
    To Do: calculate the multiplication result of all values using functools.reduce() 
           from the standard library and a lambda function.
"""
lst_5 = [1, 2, 3, 4, 5]

res_5 = functools.reduce(lambda x, y: x * y, lst_5)
print(f"Task 5 - Result: {res_5}")

# BONUS TASKS
"""
    Task 6
    Condition: given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
    To Do: write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
"""
lst_6 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]

res_6 = [x for sublst in lst_6 for x in sublst]
print(f"Task 6 - Result: {res_6}")

"""
    Task 7
    Condition: given a dictionary {'a': 1, 'b': 2, 'c': 3}
    To Do: using a dict comprehension flip the dictionary (make keys from values and vice versa): 
           F.e.: {1: 'a', 2: 'b', 3: 'c'}.
"""
dct_7 = {'a': 1, 'b': 2, 'c': 3}

res_7 = {value: key for key, value in dct_7.items()}
print(f"Task 7 - Result: {res_7}")
