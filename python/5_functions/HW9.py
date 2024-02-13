def say_hello():
    """Outputs 'Hello World!'"""
    print("Hello World!")

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.
    """
    return length * width

# Test the say_hello function
say_hello()

# Test the calculate_rectangle_area function
length1, width1 = 5, 3
area1 = calculate_rectangle_area(length1, width1)
print(f"Area of rectangle with length {length1} and width {width1} is {area1}")

length2, width2 = 10, 7
area2 = calculate_rectangle_area(length2, width2)
print(f"Area of rectangle with length {length2} and width {width2} is {area2}")

length3, width3 = 2.5, 6
area3 = calculate_rectangle_area(length3, width3)
print(f"Area of rectangle with length {length3} and width {width3} is {area3}")
