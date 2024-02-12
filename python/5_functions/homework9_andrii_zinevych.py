# 1.1 Create a function without arguments that outputs "Hello World!".

def hello_world_function():
    print("Hello World!")


hello_world_function()

# 1.2 Create a function that calculates the area of a rectangle.

def calculate_rectangle_area():
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    def get_user_input():
        """
        Getting the user input
        """
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return length, width

    length, width = get_user_input()

    """
    Calculates the area of a rectangle and output the result
    """
    area = length * width
    print(f"Area of rectangle with length {length} and width {width} = {area}")
    return area


print(calculate_rectangle_area())
