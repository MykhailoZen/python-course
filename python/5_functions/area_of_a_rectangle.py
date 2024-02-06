# 1.1 Create a function without arguments that outputs "Hello World!"
def greeting() -> None:
    print("Hello World!")


greeting()

# 1.2 Create a function that calculates the area of a rectangle.
def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Returns the rectangle area calculated as multiplication of length and width

    :param length: length of rectangle
    :param width: width of rectangle
    :return int
    """
    return length * width


print(f"Rectangle area is {calculate_rectangle_area(3.5, 10)}cm")
print(f"Rectangle area is {calculate_rectangle_area(11, 7)}cm")
print(f"Rectangle area is {calculate_rectangle_area(3, 5)}cm")


