"""
Practice - coding:
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

from functools import reduce

# Mandatory Task 1: Squaring
def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

# Mandatory Task 2: Filtering even
def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Optional Task 1: Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

# Optional Task 2: Capitalizing
def capitalize_sentence(sentence):
    return ' '.join(map(lambda word: word.capitalize(), sentence.split()))

# Optional Task 3: Average score
def average_score(scores):
    total_score = sum(score for _, score in scores)
    return total_score / len(scores) if scores else 0

# Example
numbers_list = [1, 2, 3, 4, 5]
print("Squared numbers:", square_numbers(numbers_list))
print("Even numbers:", even_numbers(numbers_list))
print("Factorial of 5:", factorial(5))
sentence = "hello world, how are you?"
print("Capitalized sentence:", capitalize_sentence(sentence))
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print("Average score:", average_score(scores))
