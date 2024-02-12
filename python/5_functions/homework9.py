# 1) Hello function
def hello():
    """Prints 'Hello!' to the console."""
    print("Hello, hello, hello, how low?")


hello()  # call the function

# 2) To find the area of the rectangle:
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float or int: The area of the rectangle.

    Raises:
        ValueError: If length or width are not numeric.
    """
    if isinstance(length, (float, int)) and isinstance(width, (float, int)):
        area = abs(length * width)
        return area

    else:
        raise ValueError("Both length and width must be numeric.")


# Test the function with different inputs

print(f'The area is {calculate_rectangle_area(4, 4)}')
print(f'the area is {calculate_rectangle_area(10, -10)}')
print(f'the area is {calculate_rectangle_area(12, 24)}')
print(f'the area is {calculate_rectangle_area(25, 35)}')
