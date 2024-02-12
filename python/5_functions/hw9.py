# 1.1 Create a function without arguments that outputs "Hello World!".
def salute():
    print("Hello World!")

#1.2 Create a function that calculates the area of a rectangle.
def calculate_rectangle_area(length, width):
  #The function should accept the length and width of the rectangle as arguments and return the calculated area.
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        area = length * width
        if area > 0:
            return area
        else:
            return ("Try again! Incorrect parameters")
    else:
        return ("Try again! Incorrect parameters")

salute()
print(calculate_rectangle_area(45, 2))
print(calculate_rectangle_area(False, True))
print(calculate_rectangle_area(22, 4))
print(calculate_rectangle_area("ohohoh", 25))
print(calculate_rectangle_area(["a", "f", "i"], ["s", "a", "2"]))
print(calculate_rectangle_area(25, "ohohoh"))
print(calculate_rectangle_area(3.3, 12))
print(calculate_rectangle_area(-10, 5))

def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        area = length * width
        if area > 0:
            return area
        else:
            return ("Try again! Incorrect parameters")
    else:
        return ("Try again! Incorrect parameters")


print(calculate_rectangle_area(45, 2))
print(calculate_rectangle_area(False, True))
print(calculate_rectangle_area(22, 4))
print(calculate_rectangle_area("ohohoh", 25))
print(calculate_rectangle_area(["a", "f", "i"], ["s", "a", "2"]))
print(calculate_rectangle_area(25, "ohohoh"))
print(calculate_rectangle_area(3.3, 12))
print(calculate_rectangle_area(-10, 5))

