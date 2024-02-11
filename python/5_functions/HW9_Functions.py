#1.1 Create a function without arguments that outputs "Hello World!".
def hello():
    print("Hello World")
hello()

#1.2 Create a function that calculates the area of a rectangle.
def calculate_rectangle_area(length, width):
    """The function should return the area of the rectangle, which is calculated as multiplication of length and width."""
    return float(length) * float(width)
"""Function testing by calling it with various inputs and printing the results:"""
print("Area is ",calculate_rectangle_area(4,3))
"""expected output: Area is  12.0"""
print("Area is ", calculate_rectangle_area(10,5.5))
"""expected output: Area is  55.0"""
print("Area is ", calculate_rectangle_area("0.6","5"))
"""expected output: Area is  3.0"""

