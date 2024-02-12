def print_string():
    """The function prints 'Hello world'"""
    print("Hello World!")


def calculate_rectangle_area(length, width):
    """
    The function calculates the area of rectangle, calculated as length times width
    """
    return length * width


print_string()  # Test function print_string

# Verify that function calculate_rectangle_area works and returns the correct values. Use a and b variables as sides
a = 10
b = 20
print(f"The area of a rectangle with length {a} and width {b} is", calculate_rectangle_area(a, b))  # Expected 200
a = 2.5
b = 4
print(f"The area of a rectangle with length {a} and width {b} is", calculate_rectangle_area(a, b))  # Expected 10.0
a = 2.5
b = 2.5
print(f"The area of a rectangle with length {a} and width {b} is", calculate_rectangle_area(a, b))  # Expected 6.25




