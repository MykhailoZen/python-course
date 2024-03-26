def calculate_square(list_of_numbers):
    """Function that takes a list of numbers as input and returns a new list containing
    the square of each number using"""
    return [x ** 2 for x in list_of_numbers]


def even_numbers(input_list):
    """Function that takes a list of numbers as input and returns a new list containing only the even numbers"""
    return [x for x in input_list if x % 2 == 0]


def factorial(n):
    """Function that calculates the factorial of a number"""
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def capitalize_letter(string):
    """Capitalize the first letter of each word in a sentence"""
    words_list = string.split()
    capitalized = []
    for word in words_list:
        capitalized.append(word.capitalize())
    return " ".join(capitalized)


def average_rating(students):
    """Calculates the average score of the students in the list"""
    all_marks = 0
    for student in students:
        all_marks += student[1]
    return all_marks / len(students)


list_to_calc = [2, 20, 13, 14, 15]
print("Square of each number: ", calculate_square(list_to_calc))
print("Even numbers: ", even_numbers(list_to_calc))
print(factorial(5))
print(capitalize_letter("hello world, how are you?"))
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print("Average rating:", average_rating(scores))
