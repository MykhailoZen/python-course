''' HW 7:
Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
Create a tuple named colors with three colors of your choice.
Create a set named numbers with the numbers from 1 to 3.
Create a dictionary named person with the following key-value pairs: 'name' and age.

Add 'grape' to the fruits list.
Remove 'potato' from the fruits list.
Check if 'apple' is in the fruits list and output the result.
Calculate the length of the colors tuple and output it.
Add the number 4 to the numbers set.
Create a new key-value pair in the person dictionary (with new 'name' and age).'''

# Creating all the required instances:
fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ("red", "green", "blue")
numbers = {1, 2, 3}
person = {"John": 16}

# Executing the operations with the instances

fruits.append('grape')
print(fruits)
fruits.remove('potato')
print(fruits)


def is_in_fruits(fruit):
    if fruit not in fruits:
        print("No! " + fruit + " is not in the fruits.")
    else:
        print("Yes! " + fruit + " is in the fruits.")


is_in_fruits("apple")

print(len(colors))
numbers.add(4)
print(numbers)

person["Jack"] = 20
print(person)
