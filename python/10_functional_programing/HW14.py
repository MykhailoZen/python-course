# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.
def numbers_list(numbers):
    return list(map(lambda x: x ** 2, numbers))


numbers = [10, 25, 39, 41, 53]
numbers_list = numbers_list(numbers)
print(numbers_list)


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_numbers_list(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers_list(numbers)
print(even_numbers)


# optional:
# Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


n = 666
result = factorial(n)
print(f"The factorial of {n} is: {result}")

# Capitalize the first letter of each word in a sentence "hello world, how are you?".
sentence = "hello world, how are you?"
capitalized_sentence = sentence.title()
print(capitalized_sentence)


# Given a list of students and their marks as tuples:
def avarage_students_score(scores):
    total_score = sum(score for _, score in scores)
    return total_score / len(scores)


scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
average_score = avarage_students_score(scores)
print(f"The average score is: {average_score}")
