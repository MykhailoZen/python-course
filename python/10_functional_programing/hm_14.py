from functools import reduce


# Write a function that takes a list of numbers as input and returns a new list containing the
# square of each number using the functional approach.
def square_of_number(input_list: list):
    """
    :param input_list: list of number
    :return: square of each number
    """
    square_list = list(map(lambda i: i ** 2, input_list))
    return f'Square of each number: "{square_list}"'


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def even_number(input_list: list):
    """
    :param input_list: list of number
    :return: a new list containing only the even numbers
    """
    new_list = list(filter(lambda i: i % 2 == 0, input_list))
    return f'A new list containing only the even numbers: "{new_list}"'


# 1 Write a function that calculates the factorial of a number using the functional approach.
def factorial(n):
    result_of_fuctorial = reduce(lambda x, y: x * y, range(1, n+1), 1)
    return f'Factorial of "{n}" is "{result_of_fuctorial}"'


# 2 Capitalize the first letter of each word in a sentence "hello world, how are you?".
def capitalize(input_str: str):
    capitalize_str = input_str.title()
    return f'Capitalize the first letter of each word in a sentence: "{capitalize_str}"'


# 3 Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list.
# The function should take the list of tuples as input and return the average score.
def avarage_of_student_score(input_tuple: tuple):
    list_of_avarage_of_score = [score[1] for score in input_tuple]
    result_of_avarage_of_score = sum(list_of_avarage_of_score)/len(list_of_avarage_of_score)
    return f'The average score "{result_of_avarage_of_score}"'


if __name__ == "__main__":
    # Verification square of each number
    a = [2, 1, 4, 5, 6, 7, 3]
    print(square_of_number(a))
    # Verification returns a new list containing only the even numbers.
    print(even_number(a))

    # Verification the factorial of a number
    number = 5
    print(factorial(number))

    # Verification capitalize the first letter
    sentence = 'hello world, how are you?'
    print(capitalize(sentence))

    # Verification the function that take the list of tuples as input and return the average score
    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    print(avarage_of_student_score(scores))
