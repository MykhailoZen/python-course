
#Given a list of numbers, write a list comprehension that produces a copy of the list.
mch_list0 = [24, 42, 32, 3211, 323, 323, 125, 552, 599, 104, 10, 535]
copied_mch_list0_compr = [num for num in mch_list0]
print(copied_mch_list0_compr)

#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
mch_list1 = [i for i in range(1, 11)]
even_mch_list1_compr = [num for num in mch_list1 if num%2==0]
print(mch_list1)
print(even_mch_list1_compr)

#Solve the task above using filter() with a lambda function.
filtred_mch_list1 = filter(lambda num: num%2==0, mch_list1)
print(list(filtred_mch_list1))

#Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function. fr_list[0].sort(key=lambda x: x[1])
fr_list = [[("apple", 50), ("banana", 10), ("cherry", 30)]]
fr_list[0].sort(key=lambda lst: lst[1])
print(fr_list)

#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
import functools

mchNum_list = [1, 2, 3, 4, 5]
mchNum_list11 = functools.reduce(lambda x,y: x*y, mchNum_list)
print(mchNum_list11)

#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
li_of_li = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
li_of_li_sort = [item for inner_list in li_of_li for item in inner_list]
print(li_of_li_sort)
