# 1) Define two variables, "length" and "width," and give them the values representing the rectangle's length and width.
# 2) Compute the area of the rectangle by multiplying the values stored in the "length" and "width" variables.
# 3) Print the calculated area.
import re


def rectangle_area(length, width):
    print("The area of the rectangle = ", length * width)


def input_param(name):
    s = input("Enter the " + name + " of the rectangle: ")
    while not(re.match(r'^\d+?\.\d+?$', s) or s.isdigit()):
        print("Incorrect value!")
        s = input("Enter the " + name + " of the rectangle: ")
    else:
        return float(s)


if __name__ == '__main__':
    rectangle_area(input_param("length"), input_param("width"))
