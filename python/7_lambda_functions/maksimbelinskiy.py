from functools import reduce

# Given a list of numbers, write a list comprehension that produces a copy of the list
original_list = [1, 2, 3, 4]
copied_list = [item for item in original_list]

#Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even_list = [item for item in range(1,11) if item % 2 == 0]

#Solve the task above using filter() with a lambda function
list(filter(lambda x: x % 2 == 0, range(1,11)))

#Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
given_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(given_list, key=lambda x: x[1])

#Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce() from the standard library and a lambda function.
multi_list = [1, 2, 3, 4, 5]
mult_result = reduce(lambda a, b: a * b, multi_list)


#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]), write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
flat_list = [item for sublist in list_of_lists for item in sublist]

#Using a dict comprehension flip the dictionary (make keys from values and vice versa). For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}


#Honestly I don't understand how it works in 6 out of 7 of answers I used chatGPT