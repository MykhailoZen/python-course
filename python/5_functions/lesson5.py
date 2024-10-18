#1) Create a function without arguments that outputs "Hello World!".
def my_hello_world():
    """The hello world function prints 'Hello World' """
    print("Hello World!")

'''2) Create a function that calculates the area of a rectangle.
The function should accept the length and width of the rectangle as arguments and return the calculated area.
Additionally, include a docstring that provides a description of what it does.
Specific requirements for the exercise:
- Create a function named calculate_rectangle_area that takes two arguments: length and width.
- The function should return the area of the rectangle, which is calculated as multiplication of length and width.
- Include a docstring in the function that provides a description of the function's purpose.
- Test your function by calling it with various inputs and printing the results.

Solution should include:

The Python function calculate_rectangle_area with the required functionality and docstring.
At least three function usage examples demonstrating the use of the function with different inputs and the expected output. '''

def calculate_rectangle_area(length, width):
    ''' The function returns the rectangle area '''
    if type(length) is str or type(width) is str:
        return "Wrong data type. Please enter positive numbers"
    elif length <= 0 or width <=0:
        return "Please enter a positive numbers"
    else:
        return length * width


my_hello_world()

print(calculate_rectangle_area(15.0, -2))
print(calculate_rectangle_area(0.8, 400))
print(calculate_rectangle_area(5, 'test'))
print(calculate_rectangle_area(5, 8))