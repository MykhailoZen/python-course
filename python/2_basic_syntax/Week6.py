# Prompt the user to input the length of the rectangle
length = float(input("Enter the length of the rectangle: "))

# Prompt the user to input the width of the rectangle
width = float(input("Enter the width of the rectangle: "))

# Define a function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    # Calculate the area by multiplying length and width
    area = length * width
    
    # Print the result
    print("The area of the rectangle is:", area)

# Call the function with the user-input length and width values
calculate_rectangle_area(length, width)
