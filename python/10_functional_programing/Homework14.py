# 1. Write a function that takes a list of numbers as input and returns a new list
# containing the square of each number using the functional approach.
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))  # solved with lambda
# or def square_numbers(numbers):
#     return [x ** 2 for x in numbers]


numbers1 = [1, 2, 3, 4]
squared_numbers = square_numbers(numbers1)
print(squared_numbers)


# 2. Write a function that takes a list of numbers as input and returns a new
# list containing only the even numbers.
def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]  # solved with list comprehension


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# or numbers2 = list(range(1, 9))
print(even_numbers(numbers2))


# 3. Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# or def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)


print(factorial(3))


# 4. Capitalize the first letter of each word in a sentence "hello world, how are you?".
sentence = "hello world, how are you?"
capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split())  # solved with generator
print(capitalized_sentence)


# 5. Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.


def calculate_average_score(scores):
    total_score = sum(score for _, score in scores)
    return total_score / len(scores)


scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
average_score = calculate_average_score(scores)
print(average_score)

