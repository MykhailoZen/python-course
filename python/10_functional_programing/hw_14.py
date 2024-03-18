from functools import reduce

# Mandatory:
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
num = [1, 5, 3, 6]
squared_list = [x ** 2 for x in num]
# print(squared_list)

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
even_num = [x for x in num if x % 2 == 0]
# print(even_num)

# Optional:
# Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n+1))


# print(factorial(4))

# Capitalize the first letter of each word in a sentence "hello world, how are you?".
def capitalized_string(n):
    result = [word.capitalize() for word in n.split(' ')]
    return ' '.join(result)


# print(capitalized_string('hello world, how are you?'))

# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]


def average_scores(n):
    number_of_students = len(n)
    sum_of_scores = sum([item[1] for item in n])
    average_score = sum_of_scores / number_of_students
    return average_score


# print(average_scores(scores))
