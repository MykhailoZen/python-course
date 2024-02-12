def calculate_rectangle_area():
    """Function calculates the area of rectangle,
    which is multiplication of length and width"""
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area_of_rectangle = length * width
    return area_of_rectangle

area = calculate_rectangle_area()
print("The area of the rectangle is:", area)