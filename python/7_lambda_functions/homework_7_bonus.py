"""
Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
write a list comprehension that produces
a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
"""
from typing import List

list_of_lists = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
flattened_list: list[int] = [item for sublist in list_of_lists for item in sublist]


"""
Using a dict comprehension flip the dictionary (make keys from values and vice versa). 
For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
"""
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}

