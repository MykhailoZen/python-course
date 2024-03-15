# Mandatory:
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
def square(numbers):
    return list(map(lambda x: x**2, numbers))
numbers = [-1, 1, 9, 12, 18, 21]

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

#
# Optional:
# Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Capitalize the first letter of each word in a sentence "hello world, how are you?".
def capitalize(sentence):
    return ' '.join(map(lambda x: x.capitalize(), sentence.split()))
sentence = "hello world, how are you?"

# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.
def average_function(scores):
    if not scores:
        return 0
    total_score = sum(score[1] for score in scores)
    return total_score / len(scores)
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

# expl for ran


print(square(numbers))

print(filter_even(numbers))

print(factorial(7))


print(capitalize(sentence))


print(average_function(scores))
