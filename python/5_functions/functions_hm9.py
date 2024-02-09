# 1.1 Create a function without arguments that outputs "Hello World!".
def hello_world():
    print("Hello World!")


hello_world()


# 1.2 Create a function that calculates the area of a rectangle.


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    Parameters: length and width should be float or int.
    Returns: the area of a rectangle S = a ⋅ b.
    """
    if type(length) not in [int, float] or type(width) not in [int, float]:
        return print(f'Length "{length}" and width "{width}" should be float or int. '
                     f'Please enter float or int type.')
    else:
        area_of_rectangle = abs(length*width)
        return print(f'Area of rectangle with length "{length}" and width "{width}" = {area_of_rectangle}')


if __name__ == "__main__":
    calculate_rectangle_area('5', 6)
    calculate_rectangle_area(5.67, 90.97967)
    calculate_rectangle_area(5, -78)
    calculate_rectangle_area(True, False)
    calculate_rectangle_area([6, 8], (7, 78))
