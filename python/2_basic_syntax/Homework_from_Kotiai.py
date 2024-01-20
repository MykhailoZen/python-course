# Variant 1
length = int(input("Please type the length of the rectangle: " ))
width = int(input("Please type the width of the rectangle: " ))
rectangle_area = length * width;
print("Computed rectangle area is equal to %s" % (rectangle_area))

# Variant 2
length_1 = int(input("Please type the length of the rectangle1: " ))
width_1 = int(input("Please type the width of the rectangle1: " ))
def area(x,y):
    rec_area = x * y
    return print(("Total rectangle area is equal to %s" % (rec_area)))
area(length_1,width_1)

# Variant 3
length_2 = int(input("Please type the length of the rectangle2: " ))
width_2 = int(input("Please type the width of the rectangle2: " ))
computed_area = lambda x, y: x * y
print("Computed rectangle area is equal to %s" % (computed_area(length_2,width_2)))