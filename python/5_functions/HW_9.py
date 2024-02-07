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
    """Calculation of the area of a rectangle. The input must be digits (int, float) or the calculation will fail."""
    if isinstance(length, (float, int)) and isinstance(width, (float, int)):
        area = abs(length * width)
        return area
    elif type(length) == str or type(width) == str:
        return "The function input must be numbers, not string."
    else:
        return "Please provide correct input data. The parameters passed to the function must be numbers."

if __name__ == "__main__":
    print(calculate_rectangle_area(4, 6))
    print(calculate_rectangle_area(66.5, 80))
    print(calculate_rectangle_area(66.5, 88.3))
    print(calculate_rectangle_area(66, 81.3))
    print(calculate_rectangle_area(5, -22))
    print(calculate_rectangle_area(-7, -23))
    print(calculate_rectangle_area(4, -18))
    print(calculate_rectangle_area("a", -22))
    print(calculate_rectangle_area(33, "b"))
    print(calculate_rectangle_area("c", "h"))
    print(calculate_rectangle_area([33, 20], (123, 43)))
    print(calculate_rectangle_area(12, (23, 14)))
    print(calculate_rectangle_area([17, 21], -4))