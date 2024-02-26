from functools import reduce

# Practice (8 points for each):

# 1. Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
copy_numbers = [x for x in numbers]
print(f"Practice point 1 \ncopy_numbers: {copy_numbers}\n")

# 2. Given a list of numbers (e.g. range(1,11)), write a list comprehension that produces a list of only the even numbers.
list_of_even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Practice point 2 \nlist_of_even_numbers: {list_of_even_numbers}\n")

# 3. Solve the task above using filter() with a lambda function.
even_num_lambda = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(f"Practice point 3 \neven_num_lambda: {even_num_lambda}\n")

# 4. Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
unsorted_list = [("apple", 50), ("banana", 10), ("cherry", 30)]

sorted_list = sorted(unsorted_list, key = lambda pair: pair[1]) # var 4.1 sorted()
print(f"Practice point 4.1 \nsorted_list with function sorted() (return new sorted copy of list): \n{sorted_list}\n")

unsorted_list.sort(key = lambda pair: pair[1]) # var 4.2 sort()
print(f"Practice point 4.2 \nsorted_list with function sort() (return changed list): \n{unsorted_list}\n")

# 5. Given the list [1,2,3,4,5], calculate the multiplication result of all values using reduce() and a lambda function.
list_of_numbers = [1, 2, 3, 4, 5]
sum_numbers_in_list = reduce(lambda x, y: x * y, list_of_numbers)
print(f"Practice point 5 \nsum_numbers_in_list: {sum_numbers_in_list}\n")

# Bonus practice (15 points for each):

# 6. Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
test_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
list_of_all_elements = [i for sublist in test_list for i in sublist]
print(f"Bonus practice 1 \nlist_of_all_elements: {list_of_all_elements}\n")

# 7. Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
test_dict = {'a': 1, 'b': 2, 'c': 3}
vice_versa_dict = {v: k for k, v in test_dict.items()}
print(f"Bonus practice 2 \nvice_versa_dict: {vice_versa_dict}")


