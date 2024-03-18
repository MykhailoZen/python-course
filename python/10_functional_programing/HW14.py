# Mandatory
# 1.Write a function that takes a list of numbers as input and returns a new list containing the square of each number
# using the functional approach.

square_num = list(map(lambda x: x ** 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 2.Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

even_num = list(filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Optional
# 1.Write a function that calculates the factorial of a number using the functional approach.

from functools import reduce
factorial = reduce(lambda x, y: x * y, range(1, 10))

# 2.Capitalize the first letter of each word in a sentence "hello world, how are you?".

cap_sentence = ' '.join([s.capitalize() for s in "hello world, how are you?".split()])

# 3.Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.

from statistics import mean

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

avr_score = mean([item[1] for item in scores])


