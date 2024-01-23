"""
This is homework for Week 6, Maksim Belinskiy
This small program calculates area of rectangle with given height and width
"""
def input_positive_float(prompt=''):
    """Get a positive float from the user"""
    while True:
        try:
            n = float(input(prompt))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, only positive floats are allowed."),
            prompt = "Please enter a positive integer: "
    return n

def area(l,w):
    """Returns an area of rectangle with given height and width"""
    return l*w


print("This program calculates the area of rectangle\n")


length = input_positive_float("Please enter height of a rectangle:\n")
width = input_positive_float("Please enter width of a rectangle:\n")

print(f'The area of rectangle with height {length} and width {width} is {area(length,width)}')
