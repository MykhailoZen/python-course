"""1.1 Create a function without arguments that outputs "Hello World!".

"""
def hello_w():
    print("Hello world!")



"""

1.2 Create a function that calculates the area of a rectangle.
The function should accept the length and width of the rectangle as arguments and return the calculated area. 
Additionally, include a docstring that provides a description of what it does.


Specific requirements for the exercise:
Create a function named calculate_rectangle_area that takes two arguments: length and width.
The function should return the area of the rectangle, which is calculated as multiplication of length and width.
Include a docstring in the function that provides a description of the function's purpose.
Test your function by calling it with various inputs and printing the results.

     

 Solution should include:

       -  The Python function calculate_rectangle_area with the required functionality and docstring.

       -  At least three function usage examples demonstrating the use of the function with different inputs and the expected output.

 """

def calculate_rectangle_area(length,width):
    print (f"you entered lenght {length} and width {width}")
    area = length * width
    print ("calculating area and returning result")
    return area


print("result:", calculate_rectangle_area(3,4))
print("result:", calculate_rectangle_area(8,4))
print("result:", calculate_rectangle_area(33,44))

