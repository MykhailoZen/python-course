from typing import Union


# 1.1 Create a function without arguments that outputs "Hello World!".
def hello_world():
    """This is function that prints Hello World!"""
    print("Hello World!")


hello_world()


# 1.2 Create a function that calculates the area of a rectangle.
# The function should accept the length and width of the rectangle as arguments and return the calculated area.
# Additionally, include a docstring that provides a description of what it does.

# Specific requirements for the exercise:
# Create a function named calculate_rectangle_area that takes two arguments: length and width.
# The function should return the area of the rectangle, which is calculated as multiplication of length and width.
# Include a docstring in the function that provides a description of the function's purpose.
# Test your function by calling it with various inputs and printing the results.

#  Solution should include:
#  -  The Python function calculate_rectangle_area with the required functionality and docstring.
#  -  At least three function usage examples demonstrating the use of the function with different inputs and
#     the expected output.


def calculate_rectangle_area(width_of_rectangle: Union[int, float],
                             length_of_rectangle: Union[int, float]) -> Union[int, float]:
    """Calculate the area of a rectangle.

    Args: width_of_rectangle and length_of_rectangle.
    Returns: calculated area -> int or float"""

    if isinstance(width_of_rectangle, (float, int)) and isinstance(length_of_rectangle, (int, float)):
        area = abs(width_of_rectangle * length_of_rectangle)
        return area
    else:
        raise ValueError('Length and width of rectangle must be int or float.')


print(f'The area is {calculate_rectangle_area(2, 3.2)}')
print(f'The area is {calculate_rectangle_area(32, 4)}')
print(f'The area is {calculate_rectangle_area(-4, 5)}')
print(f'The area is {calculate_rectangle_area(0, 7)}')
print(f'The area is {calculate_rectangle_area(5.3, 2.7)}')
