# 1. Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.

def square_list(numbers):
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    return squared_numbers

#check
numbers_list = [1, 2, 3, 4, 5]
squared_values = square_list(numbers_list)
print(f"Square of each number in list: {squared_values}")

# 2. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

def filter_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

#check
numbers_list2 = [1, 2, 3, 5, 10, 12, 0]
even_numbers_list = filter_even_numbers(numbers_list2)
print(f"List contains only the even number: {even_numbers_list}")

# 3 Optional. Given a list of students and their marks as tuples: scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.

from functools import reduce

def average_score(scores):
    total = reduce(lambda accumulator, score_in_scores: accumulator + score_in_scores[1], scores, 0) #calculating total of score using fuction reduce() for turple elements with index [1]
    quantity_students = len(scores)

    scores_avg = total / quantity_students
    return  scores_avg

#check
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
avg_score = average_score(scores)
print(f"Average score of the students in the list: {avg_score}")
