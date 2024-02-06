# 1.1 Create a function without arguments that outputs "Hello World!".

def hello_world():
    """Prints 'Hello World!' to the console."""
    print("Hello World!")

hello_world()

# 1.2 Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.
#
# Specific requirements for the exercise:
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
# Include a docstring in the function that provides a description of the function's purpose.
# Test your function by calling it with various inputs and printing the results.
#
#  Solution should include:
#  -  The Python function calculate_rectangle_area with the required functionality and docstring.
#  -  At least three function usage examples demonstrating the use of the function with different
#  inputs and the expected output.

def calculate_rectangle_area(length, width):
    """Calculation of the area of a rectangle"""
    area = abs(length * width)
    return area

print(calculate_rectangle_area(4, 6))
print(calculate_rectangle_area(66, 80))
print(calculate_rectangle_area(5, -22))