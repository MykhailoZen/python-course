import math


# Write a function that takes a list of numbers as input
# and returns a new list containing the square of each number using the functional approach.
def squared_list(list):
    return [item ** 2 for item in list]


l1 = squared_list([2,3,4,10])
print(l1)


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_list(list):
    return [item for item in list if item % 2 != 0]


l2 = even_list([1,2,3,4,5,6,7,8,9,10])
print(l2)


# Write a function that calculates the factorial of a number using the functional approach.
def factorial_list(num):
    return math.factorial(num)

l3 = factorial_list(10)
print(l3)


# Capitalize the first letter of each word in a sentence "hello world, how are you?"

def titled_words(a):
    return " ".join([i.title() for i in a.split()])

l4 = titled_words("hello world, how are you?")
print(l4)


# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

def aver_score(list):
    res = 0
    for i in list:
        res += i[1]

    return res / len(list)

l5 = aver_score(scores)
print(l5)





