# Mandatory:
# Write a function that takes a list of numbers as input and returns a new list containing
# the square of each number using the functional approach:
def square_number(numbers):
    return [x ** 2 for x in numbers]


# Write a function that takes a list of numbers as input and returns a new list containing
# only the even numbers:
def even_number (numbers):
    return [x for x in numbers if x % 2 == 0]


# Optional:
# Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    return 1 if n==0 else n * factorial(n - 1)


# Capitalize the first letter of each word in a sentence "hello world, how are you?".


# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.
def calculate_average_score(scores):
    return sum(score for _, score in scores) / len(scores)


# Execution:
numbers = [0, 1, 3, 6, 9, 14, 21, 32, 41, 58]
print("Squared numbers:", square_number(numbers))
print("Even numbers:", even_number(numbers))

n = 7
print("Factorial of", n, "is", factorial(n))

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print("Average score:", calculate_average_score(scores))