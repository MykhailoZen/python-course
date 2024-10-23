def simple_output():
    print("Hello World!")


def calculate_rectangle_area(length, width):
    """
    Calculates rectangle area by provided arguments:
    :param length: length of the rectangle in cm
    :param width: width of the rectangle in cm
    :return: area of the rectangle in cm2
    """
    if length <= 0 or width <= 0:
        return False
    return length * width


print(calculate_rectangle_area(3,4))
print(calculate_rectangle_area(0,5))
print(calculate_rectangle_area(-6,5))
print(calculate_rectangle_area(1, 7))
