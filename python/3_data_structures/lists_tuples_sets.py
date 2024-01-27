# Homework 7 Data Structures

# Creating a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
# Creating a tuple named colors with three colors of my choice.
colors = ("black", "red", "blue")
# Creating a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
# Creating a dictionary named person with the following key-value pairs: 'name' and age.
person = {"John": 30}
# Adding 'grape' to the fruits list.
fruits.append('grape')
# Removing 'potato' from the fruits list.
fruits.remove('potato')
# Checking if 'apple' is in the fruits list and output the result.
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list.")
# Calculating the length of the colors tuple and output it.
length_of_colors = len(colors)
print("Length of the colors tuple:", length_of_colors)
# Adding the number 4 to the numbers set.
numbers.add(4)
# Creating a new key-value pair in the person dictionary (with new 'name' and age).
person.update({"William": 35})
