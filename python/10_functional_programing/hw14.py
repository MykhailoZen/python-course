from functools import reduce


# 1. Write a function that takes a list of numbers as input and returns a new list
# containing the square of each number using the functional approach.
def square(numlist):
    return list(map(lambda i: i * i, numlist))

print(square([3, 5, 6, 7, 33]))


# 2. Write a function that takes a list of numbers as input and returns
# a new list containing only the even numbers.
def even(numlist):
    return list(filter(lambda i: i % 2 == 0, numlist))

print(even([1, 2, 3, 4, 5, 6, 7,]))


# 1. Write a function that calculates the factorial of a number using the functional approach.
def fact(num):
    return reduce((lambda x, y: x * y), range(1, num + 1))

print(fact(10))

# 2. Capitalize the first letter of each word in a sentence "hello world, how are you?".
def cap(text):
    return text.title()

def hello(func):
    greeting = func("hello world, how are you?")
    print(greeting)

hello(cap)


"""
3. Given a list of students and their marks as tuples:
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
Write a function that calculates the average score of the students in the list. 
The function should take the list of tuples as input and return the average score. 
"""