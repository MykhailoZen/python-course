"""
Write a function that takes a list of numbers as input and returns a new list
containing the square of each number using the functional approach.
"""

def number_list(numbers):
    return [items ** 2 for items in numbers]


numbers = [1, 5, 9, 20, 51]
number_list = number_list(numbers)
print(number_list)

# output [1, 25, 81, 400, 2601]


"""
Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
"""

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers(numbers)
print(even_numbers)

# output [2, 4, 6, 8, 10]
