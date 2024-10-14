# 1) Create a function without arguments that outputs "Hello World!".
def my_func():
    print("Hello World")


#2) Create a function that calculates the area of a rectangle
'''This function calculates the area of rectangle. It accepts the length and the width of the rectangle as arguments 
and return the calculated area'''
def calculate_rectangle_area(l, w):
    return l * w

game_running = True
while game_running:
    width = abs(float(input('Type width: ')))
    length = abs(float(input('Type length: ')))
    if width > length:
        print('Width should not be longer that length. Try again: ')
    elif (width == 0) | (length == 0):
        print("The value should not be equal to 0.")
    else:
        print(f"The area of rectangle = {calculate_rectangle_area(width, length)}.")
        game_running = False





