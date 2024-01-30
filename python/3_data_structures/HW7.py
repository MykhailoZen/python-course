# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
print(type(fruits), fruits)

# Create a tuple named colors with three colors of your choice.
colors = ('red', 'green', 'blue')
print(type(colors), colors)

# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
print(type(numbers), numbers)

# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {'name': 'John', 'age': 25}
print(type(person), person)

# Add 'grape' to the fruits list.
fruits.append('grape')
print(fruits)

# Remove 'potato' from the fruits list.
fruits.remove('potato')
print(fruits)

# Check if 'apple' is in the fruits list and output the result.
if 'apple' in fruits:
    print('Yes, apple is in the fruits list.')
else:
    print('No, apple is not in the fruits list.')

# Calculate the length of the colors tuple and output it.
print(len(colors))

# Add the number 4 to the numbers set.
numbers.add(4)
print(type(numbers), numbers)

# Create a new key-value pair in the person dictionary (with new 'name' and age).
person['new_name'] = 'Alice'
person['new_age'] = 30
print(type(person), person)
