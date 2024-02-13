def hello():
    print("Hello World")


"""This function prints Hello World"""

hello()


def calculate_rectangle_area(length_val, width_val):
    """This function calculates the area of a rectangle."""

    return length_val * width_val


# example 1
print("The area of a rectangle with length 5 and width 4 is:", calculate_rectangle_area(5, 4))  # expected 20

# example 2
print("The area of a rectangle with length 3.5 and width 2.5 is:", calculate_rectangle_area(3.5, 2.5))  # expected 8.75

# example 3
print("The area of a rectangle with length 10 and width 20 is:", calculate_rectangle_area(10, 20))  # expected 200
