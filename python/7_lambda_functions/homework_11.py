from functools import reduce

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
num_list = [1, 2, 3, 4, 5, 6, 7]
num_list2 = [x for x in num_list]
print(num_list2)

# 2. Given a list of numbers, write a list comprehension that produces a list of only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# 3. Solve the task above using filter() with a lambda function.
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(filter(lambda x: x % 2 == 0, numbers2)))

# 4. Given the list, sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
fruits.sort(key=lambda x: x[1])
print(fruits)

# 5. Given the list calculate the multiplication result of all values using reduce() and a lambda function.
nums = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, nums))

# 6. Given a list of lists write a list comprehension that produces a single list of all items
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [x for new_list in list_of_lists for x in new_list]
print(single_list)

# 7. Using a dict comprehension flip the dictionary (make keys from values and vice versa)
my_dic = {'a': 1, 'b': 2, 'c': 3}
reverse_dic = {v: k for k, v in my_dic.items()}
print(reverse_dic)
