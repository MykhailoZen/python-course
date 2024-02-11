# 1.1 task
def hello_world(): #function without arguments that outputs "Hello World!".
    print ("Hello World!")

hello_world() #check answer

#1.2 task
def calculate_rectangle_area(length, width): #function  calculate_rectangle_area that takes two arguments: length and width.
    area = length * width # the formula area of the rectangle
    return print (f"Area of the rectangle with sides {length} and {width} is {area}") # return result of function with additional test in "print"

calculate_rectangle_area(4,5) # expected the area of the rectangle 20
calculate_rectangle_area(3,1.5) # # expected the area of the rectangle 4.5
calculate_rectangle_area(1,10) # expected the area of the rectangle 10