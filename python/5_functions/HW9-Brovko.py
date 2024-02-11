def hello():
    print("Hello World!")


def calculate_rectangle_area(length, width):

    """The function calculates an area of a rectangle by multiplying the absolute values of arguments (to make sure the
     result is a positive value in case of a typo) and throws a hint in case a non-numeric argument is used"""

    if type(length) is str or type(width) is str:
        print("Please use digits only")
    else:
        print("The area of a %d by %d rectangle is " % (length, width), abs(length) * abs(width))
        return abs(length) * abs(width)


hello()
calculate_rectangle_area(4, 5)
calculate_rectangle_area(4, -5)
calculate_rectangle_area(4.5, 5)
calculate_rectangle_area(4, 555)
calculate_rectangle_area(4, "banana")
