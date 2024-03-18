"""
Mandatory:
- Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
- Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

Optional:
- Write a function that calculates the factorial of a number using the functional approach.
- Capitalize the first letter of each word in a sentence "hello world, how are you?".
- Given a list of students and their marks as tuples:
    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
"""
from functools import reduce

# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def sq_func(nums_list):
    sq_list = list(map((lambda x: x ** 2), nums_list))
    return sq_list

print(sq_func(numbers))


# 2
def ev_func(nums_list):
    ev_list = list(filter(lambda x: x % 2 == 0, nums_list))
    return ev_list

print(ev_func(numbers))


def is_even(x):
    return x % 2 == 0


def new_filter(function, nums_list):
    return reduce(lambda items, value: items + [value] if function(value) else items, nums_list, [])


print(list(new_filter(is_even, numbers)))

#3

def factorial(num):
    return reduce(lambda x, y: x * y, range(1, num + 1))

print(factorial(5))

#4
def capitalizator(text):
    return text.capitalize()

sent = "hello world, how are you?"

print(capitalizator(sent))

#5

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
l = len(scores)
sum = 0
for x in scores:
    sum += (x[1])
print("sum = " + str(sum/len(scores)))


def average_score(score):
    all_score = reduce(lambda x, y: x + y, map(lambda x: x[1], score))
    average_score = all_score / len(score)
    return average_score


result = average_score(scores)
print(result)



