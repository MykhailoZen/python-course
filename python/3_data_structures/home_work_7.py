# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
# Create a tuple named colors with three colors of your choice.
colors = ('red', 'blue', 'green')
# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {'Jack': 30, 'Steven': 25}
# Add 'grape' to the fruits list.
fruits.append('grape')
# Remove 'potato' from the fruits list.
fruits.remove('potato')
# Check if 'apple' is in the fruits list and output the result.
if 'apple' in fruits:
    print('apple is in the list')
else:
    print('apple is not in the list')
# Calculate the length of the colors tuple and output it.
print("The numbers of colors: {}".format(len(colors)))
# Add the number 4 to the numbers set
numbers.add(4)
# Create a new key-value pair in the person dictionary (with new 'name' and age).
person["John"] = 40
