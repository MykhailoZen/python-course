#1.Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1, 2, 4, 10, 5]
copy_numb = [x for x in numbers]
print (f"Copied list: {copy_numb}")

#2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
numbers2 = range(1, 15)
even_numbers = [x for x in numbers2 if x%2 == 0]
print(f"Even numbers list: {even_numbers}")

#3. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruit =  [("apple", 50), ("banana", 10), ("cherry", 30)]
sort_fruit_list = sorted(fruit, key=lambda x:x[1])
print(f"Sorted fruits list: {sort_fruit_list}")

#4. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.

import functools
numbers3 = [1, 2, 3, 4, 5]
print("Multiplication result of list:", functools.reduce(lambda x,y: x*y, numbers3) )

#Bonus
#1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[50, 41, 78], [81, 19, 26], [72, 32, 44]]
single_list = [i for new_list in list_of_lists for i in new_list]
print(f"Single list: {single_list}")






