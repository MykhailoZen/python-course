from functools import reduce


# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.

def square_numbers(numbers):
    """Squares each number in the list and returns a new list."""
    return list(map(lambda x: x ** 2, numbers))


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_numbers(numbers):
    """Filters even numbers from the list and returns a new list."""
    return list(filter(lambda x: x % 2 == 0, numbers))


# Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    """Calculates the factorial of a number using reduce function."""
    return reduce(lambda x, y: x * y, range(1, n + 1))


# Capitalize the first letter of each word in a sentence "hello world, how are you?".
def capitalize_sentence(sentence):
    """Capitalizes the first letter of each word in a sentence."""
    return " ".join(word.capitalize() for word in sentence.split())


# Given a list of students and their marks as tuples: scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78),
# ("David", 95)] Write a function that calculates the average score of the students in the list. The function should
# take the list of tuples as input and return the average score.
def average_score(scores):
    """Calculates the average score of students in the list."""
    total_score = sum(score for _, score in scores)
    return total_score / len(scores)


# Example usage
numbers = [2, 3, 6, 11, 16]
squared_numbers = square_numbers(numbers)
print(squared_numbers)  # Output: [4, 9, 36, 121, 256]

evens = even_numbers(numbers)
print(evens)  # Output: [2, 6, 16]

# Optional usage
print(factorial(7))  # Output: 5040

sentence = "hello world, how are you?"
capitalized_sentence = capitalize_sentence(sentence)
print(capitalized_sentence)  # Output: Hello World, How Are You?

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
average = average_score(scores)
print(average)  # Output: 87.5
