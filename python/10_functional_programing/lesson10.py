#Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
from functools import reduce
from math import degrees


def square_list(list):
    return [x**2 for x in list]

print(square_list([1, 3, 5]))

#Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_numbers(list):
    return [x for x in list if x%2==0]

print(even_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

#Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(4))

#Capitalize the first letter of each word in a sentence "hello world, how are you?".
def cap_letters(frase):
    return frase.title()

print(cap_letters("hello world, how are you?"))

#Given a list of students and their marks as tuples:
#scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
#Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.

def avr_score(student_scores):
   # flattened = [item for row in matrix for item in row]
    score = [x for y in student_scores for x in y][1::2]
    return float(sum(score))/len(score)


test_data = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print(avr_score(test_data))

