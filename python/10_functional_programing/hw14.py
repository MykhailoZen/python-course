
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1.Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.

def square_number(list_of_numbers):
    return list(map(lambda number: number ** 2, list_of_numbers))

print(square_number(list_of_numbers))


#2.Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

def even_number(list_of_numbers):
    return list(filter(lambda number: number % 2 == 0, list_of_numbers))

print(even_number(list_of_numbers))
