# Create a list named fruits
fruits = ['apple', 'banana', 'cherry', 'potato']

# Create a tuple named colors
colors = ('red', 'green', 'blue')

# Create a set named numbers with the numbers from 1 to 3
numbers = {1, 2, 3}

# Create a dictionary named person with initial key-value pairs
person = {'name': 'Boiko', 'age': 33}

# Add 'grape' to the fruits list
fruits.append('grape')

# Remove 'potato' from the fruits list
fruits.remove('potato')

# Check if 'apple' is in the fruits list and output the result
is_apple_in_fruits = 'apple' in fruits
print('Is "apple" in the fruits list?', is_apple_in_fruits)

# Calculate the length of the colors tuple and output it
colors_length = len(colors)
print('Length of the colors tuple:', colors_length)

# Add the number 4 to the numbers set
numbers.add(4)

# Update the person dictionary with new key-value pairs
person.update({'new_name': 'Iryna', 'new_age': 34})

# Output the updated lists, tuple, set, and dictionary
print('Updated fruits list:', fruits)
print('Updated colors tuple:', colors)
print('Updated numbers set:', numbers)
print('Updated person dictionary:', person)
