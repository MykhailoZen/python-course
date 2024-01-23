# Define two variables, "length" and "width," and give them the values representing the rectangle's length and width.
width = float(input('Enter width of rectangle: '))
length = float(input('Enter length of rectangle: '))


# Create a function to find and show the area of a rectangle with known dimensions.
def calculate_rectangle_area(width_of_rectangle: float, length_of_rectangle: float) -> float:
    # Compute the area of the rectangle by multiplying the values stored in the "length" and "width" variables.
    area = width_of_rectangle * length_of_rectangle
    # Print the calculated area.
    print(f'Area of a rectangle equal: {area}')

    return area


calculate_rectangle_area(width, length)
