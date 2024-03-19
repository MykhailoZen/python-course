"""
Mandatory:

Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
Optional:

Write a function that calculates the factorial of a number using the functional approach.
Capitalize the first letter of each word in a sentence "hello world, how are you?".
Given a list of students and their marks as tuples:

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
"""

#1.1 - Using of nested lambda and map function
def square_numbers_1(numbers):
    square_numbers_1 = list(map(lambda x: x ** 2, numbers))
    return square_numbers_1

# Example of usage:
numbers = [1, 3, 5, 7, 9]
square_numbers_1 = square_numbers_1(numbers)
print("Initial Number List:", numbers)
print("Square Number List:", square_numbers_1)
print()

#1.2 - Using of list comprehension

def square_numbers_2(numbers):
    square_numbers_2 = [x ** 2 for x in numbers]
    return square_numbers_2

# Example of usage:
numbers = [2, 4, 6, 8, 10]
square_numbers_2 = square_numbers_2(numbers)
print("Initial Number List:", numbers)
print("Square Number List:", square_numbers_2)
print()

#2 - Usage of filter() to keep only the even numbers in the list

def even_number_filter(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

# Example of usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_number_filter(numbers)
print("Initial Number List:", numbers)
print("Filtered Numbers to keep only even:", even_numbers)
print()

#Optional

#3 - Factorial, usage of reduce() and range()

from functools import reduce

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

# Example of usage:
number = 4
result = factorial(number)
print(f"The factorial of {number} is:", result)
print()

#4 - Use map() with nested str.capitalize() to make capitalized the first letter of each word

message = "hello world, how are you?"

capitalized_message = ' '.join(map(str.capitalize, message.split()))

print("Original Message:", message)
print("Capitalized Message:", capitalized_message)
print()


#5 - Calculation the sum of scores for all students using list comprehension and unpacking of variables replaciung uninterested one with _

def calculate_average_score(scores):
    total_score = sum([score for _, score in scores])
    num_students = len(scores)
    average_score = total_score / num_students

    return average_score


# Example of usage:
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
average_score = calculate_average_score(scores)
print (scores)
print("Average Score for all students:", average_score)
