# Lesson 5
# Homework 1
# Exercise 1
# A function without arguments that outputs "Hello World!".

def hello_world():
    print("Hello World!")

# Exercise 2
# A function that calculates the area of a rectangle.

def calculate_rectangle_area(length,width):
    try:
        if length < 0 or width < 0:
            return "Width and length cannot be negative"
        else:
            return length*width
    except TypeError:
        return "Width and length have to be numbers"

hello_world()

print(calculate_rectangle_area(5,6))
print(calculate_rectangle_area(5.99,6.3))
print(calculate_rectangle_area(5,0))
print(calculate_rectangle_area(0,0))
print(calculate_rectangle_area(-1,6))
print(calculate_rectangle_area(-1,0))
print(calculate_rectangle_area(5,"Elephant"))

