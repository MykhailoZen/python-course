#1) Define two variables, "length" and "width," and give them the values representing the rectangle's length and width.
#2) Compute the area of the rectangle by multiplying the values stored in the "length" and "width" variables.
#3) Print the calculated area.

length = 7
width = 5
rectangle_area = length*width
print("The rectangle area is: " + str(rectangle_area))


def rectangle_area(length, width):
    area = length * width
    return area

print("The rectangle area is: " + str(rectangle_area(7, 5)))
