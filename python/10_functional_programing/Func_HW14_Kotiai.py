'''
1. Write a function that takes a list of numbers as input and returns
a new list containing the square of each number using the functional approach.
'''


def square(lst):
    return list(map(lambda x: x * x, lst))


print(square([11, 12, 21]))

'''
2. Write a function that takes a list of numbers as input and returns 
a new list containing only the even numbers.
'''


def even_lst(lst):
    return list(filter(lambda x: x % 2 == 0, lst))


print(even_lst([11, 12, 21, 23, 34, 37, 24, 22, 10]))

'''
Write a function that calculates the factorial of a number using the functional approach.
'''


def factorial_1(num):
    from functools import reduce
    return reduce((lambda x, y: x * y), range(1, num + 1))


print(factorial_1(5))

'''
Capitalize the first letter of each word in a sentence "hello world, how are you?".
'''


def capit(s):
    return ' '.join(map(lambda x: x.capitalize(), s.split()))


print(capit("hello world, how are you?"))

'''
Given a list of students and their marks as tuples:

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
Write a function that calculates the average score of the students in the list. 
The function should take the list of tuples as input and return the average score. 
'''


# Solution 1
def average(lst):
    scores = list(map(lambda x: x[1], lst))
    '''Avoiding division by zero'''
    if len(scores) == 0:
        return 0
    from functools import reduce
    return reduce(lambda x, y: x + y, scores) / len(lst)


print(average([("Alice", 85), ("Bob", 96), ("Charlie", 90), ("David", 105)]))


# Solution 2
def average_1(lst):
    scores = list(map(lambda x: x[1], lst))
    '''Avoiding division by zero'''
    if len(scores) == 0:
        return 0
    return sum(scores) / len(lst)


print(average_1([("Alice", 4), ("Bob", 8), ("Charlie", 12), ("David", 20)]))
