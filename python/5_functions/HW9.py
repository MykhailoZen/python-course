# Task 1.1
def greetings():
    print("Hello World!")


greetings()


# Task 1.2
def calculate_rectangle_area(length, width):
    """This function calculates rectangle area by multiplying length and width and then return the result"""
    result = length * width
    return result


print(f"width = 5, height = 10, result = {calculate_rectangle_area(5, 10)}, expected = 50")
print(f"width = 4.5, height = 5.2, result = {calculate_rectangle_area(4.5,5.5)}, expected = 24.75")
print(f"width = 234, height = 567, result = {calculate_rectangle_area(234, 567)}, expected = 132678")
