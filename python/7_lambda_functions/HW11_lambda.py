'''
1. Given a list of numbers, write a list comprehension that produces a copy of the list.
'''
number_list = [x for x in range(10)]
print(number_list)
'''
Copy of the number_list using the expression:
'''
cp_number_list = [x for x in number_list]
print(cp_number_list)

'''
2. Given a list of numbers (e.g. range(1, 11)), write a list 
comprehension that produces a list of only the even numbers.
'''
lst_num = [x for x in range(1, 11)]
print(lst_num)
even_numbers = [x for x in lst_num if x % 2 == 0]
print(even_numbers)

'''
3. Solve the task above using filter() with a lambda function.
'''
lst_num_1 = [x for x in range(1, 11)]
even_numbers_1 = list(filter(lambda x: x % 2 == 0, lst_num_1))
print(even_numbers_1)

'''
4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], 
sort it by the number using the lambda function.
'''

l = [("apple", 50), ("banana", 10), ("cherry", 30)]
l.sort(key=lambda x: x[1])
print(l)

'''
5. Given the list [1, 2, 3, 4, 5], 
calculate the multiplication result of all values using reduce() and a lambda function.
'''
from functools import reduce
ls = [1, 2, 3, 4, 5]
mlt = reduce(lambda x,y: x * y, ls)
print(mlt)

'''
Bonus practice (15 points for each):

1. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), 
write a list comprehension that produces a single list of all 
items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
'''

lst_6 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
lst_single = [j for i in lst_6 for j in i]
print(lst_single)

'''
2. Using a dict comprehension flip the dictionary (make keys from values and vice versa).
 For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
'''
dic_origin = {'a': 1, 'b': 2, 'c': 3}
dic_flip = dict([(x, y) for y, x in dic_origin.items()])
print(dic_flip)