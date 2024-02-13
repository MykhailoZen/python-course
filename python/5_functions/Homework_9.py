def greeting():
    print("Hello World!")
def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.
    Parameters:
    length : The length of the rectangle.
    width : The width of the rectangle.
    Returns:
    The area of the rectangle, calculated as the product of length and width.
    """
    area = length * width
    return area

area1 = calculate_rectangle_area(5, 6)
print("Area 1:", area1)

area2 = calculate_rectangle_area(6.5, 4.5)
print("Area 2:", area2)

area3 = calculate_rectangle_area(15, 30)
print("Area 3:", area3)