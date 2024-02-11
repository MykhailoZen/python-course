# 1.1Create a function without arguments that outputs "Hello World!".
def my_world():
    print("Hello World!")


my_world()


# 1.2 Create a function that calculates the area of a rectangle.
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float or int: The calculated area of the rectangle.
    """
    return length * width


# Test the function with different inputs
print("The fist rectangle area is: ", calculate_rectangle_area(13, 14))
print("The second rectangle area is: ", calculate_rectangle_area(11.7, 16.5))
print("The third rectangle area is: ", calculate_rectangle_area(width=13, length=14))

