# Write a function that takes a list of numbers as input
# and returns a new list containing the square of each number using the functional approach
def square_of_each_number(numbers):
    return [number ** 2 for number in numbers]


numbers = [1, 4, 6, 7, 12, 15, 33, 18]
square_numbers = square_of_each_number(numbers)
print(square_numbers)


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_numbers(square_numbers):
    return [number for number in square_numbers if number % 2 == 0]


even_number = even_numbers(square_numbers)
print(even_number)


# Capitalize the first letter of each word in a sentence "hello world, how are you?".
def capitalize_first_letter(sentence):
    return sentence.title()


print(capitalize_first_letter("hello world, how are you?"))


# Given a list of students and their marks as tuples:
def average_score(scores):
    score_sum = sum(score for _, score in scores)
    students_count = len(scores)
    return score_sum / students_count if students_count > 0 else 0

# Example usage
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
average_s = average_score(scores)
print(f"The average score for students is: {average_s}")