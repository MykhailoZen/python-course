def print_hello():
    print("Hello World!")

print_hello()

def calculate_rectangle_area(length, width):
    """
    The function calculates the area of rectangle.
    Multiply length by width and return result
    """

    return length * width

print(calculate_rectangle_area(5, 6)) # Expected 30

a = 10
b = 15
print(calculate_rectangle_area(a, b)) # Expected 150

result = calculate_rectangle_area(7, 8) # Expected 56
print("The area is:", result)