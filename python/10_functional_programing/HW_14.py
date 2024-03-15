from functools import reduce
from math import factorial

def check_empty_list(func):
    """Decorator to check if a list is empty."""
    def wrapper(list_of_value):
        if not list_of_value:
            raise ValueError("List is empty")
        return func(list_of_value)
    return wrapper

# Practice - coding:
#
# Mandatory:
#
# Write a function that takes a list of numbers as input and returns a new list containing the square of each
# number using the functional approach.
list_of_numbers = [1, 3, 5, 7, 9]

@check_empty_list
def square_of_numbers_pow(list_of_num):
    return list(map(lambda x: pow(x, 2), list_of_num))

print(f"list square of numbers with pow(): \n{square_of_numbers_pow(list_of_numbers)}")

@check_empty_list
def square_of_numbers(list_of_num):
    return list(map(lambda x: x ** 2, list_of_num))

print(f"list of square numbers: \n{square_of_numbers(list_of_numbers)}")

@check_empty_list
def square_of_numbers_list_comp(list_of_num):
    return [x ** 2 for x in list_of_num]

print(f"list square of numbers with list comprehension: \n{square_of_numbers_list_comp(list_of_numbers)}")

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
list_of_numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

@check_empty_list
def even_number_filter(list_of_num):
    return list(filter(lambda x: not x % 2, list_of_num))

print(f"list of even numbers with filter(): \n{even_number_filter(list_of_numbers2)}")

@check_empty_list
def even_number_list_comp(list_of_num):
    return [x for x in list_of_num if not x % 2]

print(f"list of even numbers with list comprehension: \n{even_number_list_comp(list_of_numbers2)}")

# Optional:
#
# Write a function that calculates the factorial of a number using the functional approach.
number = 0
def my_factorial(number):
    return factorial(number)

print(f"Calculating factorial number with factorial(): \n{my_factorial(number)}")

def my_factorial_reduce(number):
    return reduce(lambda x, y: x * y, range(1, number + 1), 1)

print(f"Calculating factorial number with reduce(): \n{my_factorial_reduce(number)}")

# Capitalize the first letter of each word in a sentence "hello world, how are you?".
phrase = "hello world, how are you?"
def capitalize_each_first_letter_title(phrase):
    return phrase.title()

print(f"capitalize phrase with title(): \n{capitalize_each_first_letter_title(phrase)}")

def capitalize_each_first_letter(phrase):
    return ' '.join(word.capitalize() for word in phrase.split())
print(f"capitalize phrase with capitalize(): \n{capitalize_each_first_letter(phrase)}")

# Given a list of students and their marks as tuples:
#
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

@check_empty_list
def average_score(list_of_tuples):
    total_score = sum(x[1] for x in list_of_tuples)
    average = total_score / len(list_of_tuples)
    return average

print(f"average score is: \n{average_score(scores)}")

@check_empty_list
def average_score_map(list_of_tuples):
    total_score = sum(map(lambda x: x[1], list_of_tuples))
    average = total_score / len(list_of_tuples)
    return average

print(f"average score calculated with map is: \n{average_score_map(scores)}")