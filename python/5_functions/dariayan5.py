def hello_world():
    print("Hello World!")

def calculate_rectangle_area(length, width):
    """
    Function return the value of area of a rectangle.
    length: length of side
    width: width of side
    """
    return length * width

hello_world()

rectangle_area = calculate_rectangle_area(1.3,45)
print(rectangle_area)

rectangle_area = calculate_rectangle_area(3,4.33)
print(rectangle_area)

rectangle_area = calculate_rectangle_area(15,7)
print(rectangle_area)
