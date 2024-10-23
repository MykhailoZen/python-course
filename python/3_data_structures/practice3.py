# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
# Create a tuple named colors with three colors of your choice.
# Create a set named numbers with the numbers from 1 to 3.
# Create a dictionary named person with the following key-value pairs: 'name' and age.
# Add 'grape' to the fruits list.
# Remove 'potato' from the fruits list.
# Check if 'apple' is in the fruits list and output the result.
# Calculate the length of the colors tuple and output it.
# Add the number 4 to the numbers set.
# Create a new key-value pair in the person dictionary (with new 'name' and age).
# Make sure to perform these operations using the basic capabilities of the data structures
# (without using comprehensions, lambdas, functions or other advanced features).

fruits = ['apple', 'banana', 'cherry', 'potato']

colors = ('orange', 'green', 'blue')
numbers = {1, 2, 3}
person = {
    "Olha": 25
}

fruits.append('grape')
fruits.remove('potato')
print(fruits)

if 'apple' in fruits:
    print("Yes, there is an apple in the fruits list")

print(len(colors))

numbers.add(4)
print(numbers)

person['Hanna'] = 26
print(person)
