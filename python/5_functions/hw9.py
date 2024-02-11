# 1.1 Create a function without arguments that outputs "Hello World!".
def greeting():
    """This will print 'Hello World!'"""
    print("Hello World!")


greeting()

'''
1.2 Create a function that calculates the area of a rectangle.

(The function should accept the length and width of the rectangle as arguments and return 
the calculated area. 
Additionally, include a docstring that provides a description of what it does.)

Specific requirements for the exercise:
    Create a function named calculate_rectangle_area that takes two arguments: length and width.
    The function should return the area of the rectangle, which is calculated as multiplication of length and width.
    Include a docstring in the function that provides a description of the function's purpose.
    Test your function by calling it with various inputs and printing the results.
     
Solution should include:
    The Python function calculate_rectangle_area with the required functionality and docstring.
    At least three function usage examples demonstrating the use of the 
    function with different inputs and the expected output.'''


def calculate_rectangle_area(length, width):
    """Calculates the rectangle area with 2 known parameters"""
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        area = length * width
        if area > 0:
            return area
        else:
            return ("Wrong parameters entered, try again!")
    else:
        return ("Wrong parameters entered, try again!")

print(calculate_rectangle_area(3, 3))
print(calculate_rectangle_area(45, 16))
print(calculate_rectangle_area(33.3, 55.5))
print(calculate_rectangle_area(-34, 45))
print(calculate_rectangle_area("dsdsds", 45))
print(calculate_rectangle_area(55, "fdfddfdsf"))
print(calculate_rectangle_area(True, False))
print(calculate_rectangle_area(["f" , "y"], ["s", "a"]))






