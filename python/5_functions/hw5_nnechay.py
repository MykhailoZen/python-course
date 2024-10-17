# 1) Create a function without arguments that outputs "Hello World!".
#
# 2) Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.
# Specific requirements for the exercise:
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
# Include a docstring in the function that provides a description of the function's purpose.
# Test your function by calling it with various inputs and printing the results.
# Solution should include:
# The Python function calculate_rectangle_area with the required functionality and docstring.
# At least three function usage examples demonstrating the use of the function with different inputs and the expected output.

import random

# Creating a function without arguments that outputs "Hello World!" (1)
def hello_func():
    print('"Hello World!"')

hello_func()

# Creating a function that calculates the area of a rectangle. (2)
def calculate_rectangle_area(length, width):
    rec_area = length * width
    return rec_area

# Usage1: calculation of the area for constant length and width to give example for user how it works
print('This script calculates a rectangle area, e.g. here is an example of calculation for a 5x8 rectangle:', calculate_rectangle_area(5,8))

# Usage: calculation of the area for random length and width
rand_length = random.randint(1, 25)
rand_width = random.randint(1, 25)
print(f'Also, here is an example of a rectangle area calculation for random length and width\nWhere length is {rand_length} and width is {rand_width}')
print('The calculated area is', calculate_rectangle_area(rand_length, rand_width))

# Usage3: calculation of the area for length and width provided by user
try:
    user_length = int(input('Enter length:'))
    user_width = int(input('Enter width:'))
    if user_length > 0 and user_width > 0:
        print('Area of your rectangle is', calculate_rectangle_area(user_length, user_width))
    else: print('Incorrect parameters!')
except: print('Incorrect parameters!')