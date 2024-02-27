# 1
original_numbers = [1, 2, 3, 4, 5]
copy_numbers = [element for element in original_numbers]
# 2
range_of_numbers = range(1, 11)
even_numbers_list_comp = [number for number in range_of_numbers if number % 2 == 0]
# 3
even_numbers_filter = list(filter(lambda number: number % 2 == 0, range(1, 11)))
# 4
fruit_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruit_list = sorted(fruit_list, key=lambda fruit: fruit[1])
# 5
from functools import reduce
num_list = [1, 2, 3, 4, 5]
multiplication_result = reduce(lambda a, b: a * b, num_list)
# 6
complex_list = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
single_list = [item for sublist in complex_list for item in sublist]
# 7
original_dictionary = {'a': 1, 'b': 2, 'c': 3}
inverted_dictionary = {value: key for key, value in original_dictionary.items()}

