# Mandatory:
#
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.

from functools import reduce
test_list = [1, 2, 3, 4, 5]


def all_squared(data: list):
    return list(map(lambda x: x*x, data))


#print(all_squared(test_list))


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

def even_only(data: list):
    return list(filter(lambda x: x % 2 == 0, data))


#print(even_only(test_list))

# Optional:
#
# Write a function that calculates the factorial of a number using the functional approach.


def factorial(data: int):
    return reduce(lambda x, y: x*y, range(1, data+1))


#print(factorial(5))

# Capitalize the first letter of each word in a sentence "hello world, how are you?".

sentence = "hello world, how are you?"


def capitalize(data: str):
    return ' '.join(map(lambda word: word.capitalize(), data.split()))


#print(capitalize(sentence))

# Given a list of students and their marks as tuples:

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of
# tuples as input and return the average score.


def average_score(data: list):
    total = 0
    for item in data:
        total += item[1]

    return total/len(data)


#print(average_score(scores))