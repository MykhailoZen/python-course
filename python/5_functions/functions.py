# Practice:
# 1) Create a function without arguments that outputs "Hello World!".
# 2) Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.
#
# Specific requirements for the exercise:
#
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
#
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
#
# Include a docstring in the function that provides a description of the function's purpose.
#
# Test your function by calling it with various inputs and printing the results.
#
# Solution should include:
#
# The Python function calculate_rectangle_area with the required functionality and docstring.
# At least three function usage examples demonstrating the use of the function with different inputs and the expected output.

def my_function() -> None:
    """
    printing of Hello, World!
    @return: None
    """
    print("Hello World")

def calculate_rectangle_area(length: int, width: int) -> int:
    """
    counts the area of a rectangle.
    @param length: the length of the rectangle
    @param width: the width of the rectangle
    @return: the area of a rectangle with specific values
    """
    return length * width

if __name__ == '__main__':
    my_function()
    print(f'Rectangle area = {calculate_rectangle_area(2, 5)}')
    print(f'Rectangle area = {calculate_rectangle_area(567, 234)}')
    print(f'Rectangle area = {calculate_rectangle_area(90, 56)}')
