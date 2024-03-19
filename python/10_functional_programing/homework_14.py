# 1. Write a function that takes a list of numbers as input and returns a new list containing
# the square of each number using the functional approach.

my_list = [1, 2, 3, 4, 5, 6]

def square_maker(list):
    square_list = [number * number for number in list]
    return square_list

print(square_maker(my_list))


# 2. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

def even_counter(list):
    even_list = [number for number in list if number % 2 == 0]
    return even_list

print(even_counter(my_list))

#Optional

#Write a function that calculates the factorial of a number using the functional approach.

def factorial_finder(num, factorial=1):
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial for number {num} is: ", factorial)

factorial_finder(4)
factorial_finder(5)
