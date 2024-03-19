"""Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach."""

def list_sqaure(input_list):
    new_square_list = []
    for x in input_list:
        x = x * x
        new_square_list.append(x)
    return new_square_list



"""Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
"""

def list_even(input_list):
    new_even_list = []
    for x in input_list:
        if x % 2 != 0:
            new_even_list.append(x)
    return new_even_list



default_list = [1, 2, 5, 7, 8, 9]
#print(list_sqaure(default_list))
#print(list_even(default_list))

"""Write a function that calculates the factorial of a number using the functional approach.
"""

def calc_factorial(input_number):
    temp_number = 1
    for x in range(1, input_number + 1):
        temp_number = x * temp_number
    result = temp_number
    return result

#print(calc_factorial(3))

"""Capitalize the first letter of each word in a sentence "hello world, how are you?"."""

def capitalize_letter(input_text):
    split_words = input_text.split(" ")
    capitalized_list = []
    for word in split_words:
        capitalized_word = word[0].upper() + word[1:]
        capitalized_list.append(capitalized_word)
    capitalized_sentence = " ".join(capitalized_list)
    return capitalized_sentence


#print(capitalize_letter("hello world, how are you?"))


"""Given a list of students and their marks as tuples:

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score. 
"""

def calculate_avg(input_tuple):
    score_list = []
    for x in input_tuple:
        score = int(x[1])
        score_list.append(score)
    score_sum = sum(score_list)
    score_avg = score_sum / len(score_list)
    return score_avg

my_tuple = [("Alice", 100), ("Bob", 92), ("Charlie", 78), ("David", 95)]

print(calculate_avg(my_tuple))