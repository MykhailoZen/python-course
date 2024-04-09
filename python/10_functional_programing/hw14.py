#Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
def sq_n(numbers):
    return list(map(lambda x: x**2, numbers))

lst0 = [2, 5, 4, 11, 22]

sed_nums = sq_n(lst0)
print(sed_nums)

#Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def fl_nums(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ev_n = fl_nums(lst1)
print(ev_n)

#Write a function that calculates the factorial of a number using the functional approach.
from functools import reduce


def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

number = 5
result = fact(number)
print(f"The factorial of {number} is {result}")

#Capitalize the first letter of each word in a sentence "hello world, how are you?".
sent = "hello world, how are you?"

capit_sent = ' '.join(map(lambda x: x.capitalize(), sent.split(' ')))
print(capit_sent)

#Given a list of students and their marks as tuples:
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

def avg_calc(scores):
    total_score = reduce(lambda x, y: x + y[1], scores, 0)
    return total_score / len(scores)

avg_score = avg_calc(scores)
print("Average score:", avg_score)
