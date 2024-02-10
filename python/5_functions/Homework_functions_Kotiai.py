"""1.1 Create a function without arguments that outputs "Hello World!".

Solution:
Firstly, define the function. Let's call it: my_function"""


def my_function():
    """This function doesn't contain any argument,
    so we just need to print the 'Hello World' text message"""
    print("Hello World")


"""1.2 Create a function that calculates the area of a rectangle.
The function should accept the length and width of the rectangle as 
arguments and return the calculated area. Additionally, include a 
docstring that provides a description of what it does.

Solution:
1. Create a function named calculate_rectangle_area that takes two 
   arguments: length and width."""


def calculate_rectangle_area(length, width):
    """2. This function should return the area of the rectangle,
    which is calculated as multiplication of length and width:"""
    rec_area = float(length) * float(width)
    return print(f"Total rectangle area is equal to {rec_area}")


"""4.Test your function by calling it with various inputs and printing the results.
   At least three function usage examples demonstrating the use of the 
   function with different inputs and the expected output.
Test #1. Call function with integer arguments:"""
calculate_rectangle_area(27, 44)
"""Expected result: 1188.0"""

"""Test #2. Call function with float arguments:"""
calculate_rectangle_area(22.5, 44.5)
"""Expected result: 1001.25"""

"""Test #3. Call function with string arguments:"""
calculate_rectangle_area("45", "34")
"""Expected result: 1530.0"""
