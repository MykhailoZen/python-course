#1.1 Create a function without arguments that outputs "Hello World!".
def hello():
    print("Hello World")
hello()

def calculate_rect_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle, calculated as length * width.
    """
    return length * width

# Expl 1
length1 = 5
width1 = 3
area1 = calculate_rect_area(length1, width1)
print(f"The area of the rectangle with length {length1} and width {width1} is: {area1}")

# Expl 2
length2 = 7.5
width2 = 4.2
area2 = calculate_rect_area(length2, width2)
print(f"The area of the rectangle with length {length2} and width {width2} is: {area2}")

# Expl 3
length3 = 10
width3 = 10
area3 = calculate_rect_area(length3, width3)
print(f"The area of the rectangle with length {length3} and width {width3} is: {area3}")