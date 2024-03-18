# Mandatory:
# 1. Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sqr():
    print("New list containing the square of each number:", [item**2 for item in t])
sqr()
# 2. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even():
    nums_even = [x for x in t if x % 2 == 0]
    return nums_even
print("List of only the even numbers:", even())


# Optional:
# 1. Write a function that calculates the factorial of a number using the functional approach.
from functools import reduce
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(5))


# 2. Capitalize the first letter of each word in a sentence "hello world, how are you?".
def cap(sentence):
    capitalizing = ' '.join(word.capitalize() for word in sentence.split())
    return capitalizing
print(cap("hello world, how are you?"))
# 3. Write a function that calculates the average score of the students in the list

def average(list):
    return sum(score for student, score in list) / len(list)

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print("Average score of the students in the list: ", average(scores))