# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
list = [1, 2, 3, 4, 5]
list_copy = list[:]
print('Copy of number list [1, 2, 3, 4, 5]: ')
print(list_copy)

list_str = ['apple', 'banana', 'cherry']
list_str_copy = list_str[:]
print('Copy of str list [\'apple\', \'banana\', \'cherry\']: ')
print(list_str_copy)

# 2. Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
list2 = range(1, 11)
list_even = [num for num in list2 if num % 2 == 0]
print('Even numbers: ')
print(list_even)

# 3. Solve the task above using filter() with a lambda function.
list_even2 = filter(lambda num: num % 2 == 0, list2)
print(type(list_even2))
print('Even numbers using filter(): ')
for num in list_even2:
    print(num)


# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
my_list =  [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print('Sorted list [("apple", 50), ("banana", 10), ("cherry", 30)] by numbers: ')
print(sorted_list)

# 5. Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
import functools

list3 =  [1, 2, 3, 4, 5]
mult = functools.reduce(lambda x, y: x * y, list3)
print('Multiplied list [1, 2, 3, 4, 5]: ')
print(mult)

# 6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).

list4 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
list_all = [num for temp_list in list4 for num in temp_list]
#for num in list4:
#   for x in num:
#        list_all.append(x)

print('List comprehension: ')
print(list_all)

# 7. Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
dict = {'a': 1, 'b': 2, 'c': 3}

dict_result = {}
for k, v in dict.items():
    dict_result[v] = k
print('Dictionary flip using for: ')
print(dict_result)

dict_r={value:key for (key,value) in dict.items()}
print('Dictionary comprehension: ')
print(dict_r)

