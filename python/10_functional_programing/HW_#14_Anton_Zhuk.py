# Write a function that takes a list of numbers as input and returns a new list containing the square of
# each number using the functional approach.
from math import factorial

first_list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def list_square_of_number(numbers_list):
    return [x ** 2 for x in numbers_list]


print(f'New list with square of each number: {list_square_of_number(first_list_of_numbers)}')

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
second_list_of_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def list_even_number(numbers_list):
    return list(filter(lambda x: x % 2 == 0, numbers_list))


print(f'New list with even numbers: {list_even_number(second_list_of_numbers)}')

# Write a function that calculates the factorial of a number using the functional approach.
num = 5


def calculate_factorial(number):
    return factorial(number)


print(f'Factorial of number {num} = {calculate_factorial(num)}')

# Capitalize the first letter of each word in a sentence "hello world, how are you?".

sentence = 'hello world, how are you?'


def capitalize_the_first_letter_of_each_word(w_sentence):
    return w_sentence.title()


print(f'Capitalize sentense: {capitalize_the_first_letter_of_each_word(sentence)}')

# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]


def calculate_average_score(list_of_students):
    total = sum(x[1] for x in list_of_students)
    average_score = total / len(list_of_students)
    return average_score


print(f'Average score of the students = {calculate_average_score(scores)}')