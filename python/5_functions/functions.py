def say_hello():
    """Prints 'Hello World!' to the console."""
    print("Hello World!")


def calculate_rectangle_area(length, width):
    """
    This function calculates the area of a rectangle.

    Arguments:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


# Testing say_hello function
say_hello()

# Testing calculate_rectangle_area function
# Example 1
length1 = 3
width1 = 7
print("Area of rectangle with length", length1, "and width", width1, "is:", calculate_rectangle_area(length1, width1))

# Example 2
length2 = 3.0
width2 = 5.5
print("Area of rectangle with length", length2, "and width", width2, "is:", calculate_rectangle_area(length2, width2))

# Example 3
length3 = 8.06732
width3 = 15.92143
print("Area of rectangle with length", length3, "and width", width3, "is:", calculate_rectangle_area(length3, width3))
