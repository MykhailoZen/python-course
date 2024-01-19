# Practice:
# Create a function to find and show the area of a rectangle with known dimensions. Here's what you need to do:
#
# 1) Define two variables, "length" and "width," and give them the values representing the rectangle's length and width.
# 2) Compute the area of the rectangle by multiplying the values stored in the "length" and "width" variables.
# 3) Print the calculated area.

def rectangle_area(x, y):
    """Calculation of the area of a rectangle"""
    length, width = x, y
    area = length * width
    print("Rectangle area: {}".format(area))
    return area

rectangle_area(4, 6)



