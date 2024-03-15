from functools import reduce
from math import factorial
# Practice - coding:
#
# Mandatory:
#
# Write a function that takes a list of numbers as input and returns a new list containing the square of each
# number using the functional approach.
list_of_numbers = [1, 3, 5, 7, 9]
list_of_square_numbers = list(map(lambda x: x ** 2, list_of_numbers))
list_of_square_numbers_var2 = list(map(lambda x: pow(x, 2), list_of_numbers))
list_of_square_numbers_var3 = [x ** 2 for x in list_of_numbers]
print(f"list_of_square_numbers: {list_of_square_numbers}")
print(f"list_of_square_numbers_var2: {list_of_square_numbers_var2}")
print(f"list_of_square_numbers_var3: {list_of_square_numbers_var3}")

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
list_of_numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_even_numbers = list(filter(lambda x: not x % 2, list_of_numbers2))
list_of_even_numbers_var2 = [x for x in list_of_numbers2 if not x % 2]
print(f"list_of_even_numbers: {list_of_even_numbers}")
print(f"list_of_even_numbers_var2: {list_of_even_numbers_var2}")

# Optional:
#
# Write a function that calculates the factorial of a number using the functional approach.
number = 0
factorial_number = reduce(lambda x, y: x * y, range(1, number + 1), 1)
print(f"factorial_number: {factorial_number}")
factorial_number2 = factorial(number)
print(f"factorial_number2: {factorial_number2}")

# Capitalize the first letter of each word in a sentence "hello world, how are you?".
phrase = "hello world, how are you?"
capitalize_phrase = phrase.title()
capitalize_phrase_var2 = ' '.join(word.capitalize() for word in phrase.split())
print(f"capitalize_phrase: {capitalize_phrase}")
print(f"capitalize_phrase_var2: {capitalize_phrase_var2}")

# Given a list of students and their marks as tuples:
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.