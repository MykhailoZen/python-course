# Practice:
# Make sure to perform these operations using the basic capabilities of the data structures
# (without using comprehensions, lambdas, functions or other advanced features).

# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']

# Create a tuple named colors with three colors of your choice.
colors = ('green', 'red', 'yellow', 'purple')

# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}

# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "Anton": 34,
    "Andrey": 61,
    "Artem": 42,
    "Elena": 63,
  }

# Add 'grape' to the fruits list.
fruits.append('grape')

# Remove 'potato' from the fruits list.
fruits.remove('potato')

# Check if 'apple' is in the fruits list and output the result.
value = 'apple'
if value in fruits:
    print(f'{value} contained in the list.')
else:
    print(f'{value} not contained in the list.')

# Calculate the length of the colors tuple and output it.
length_of_colors = len(colors)
print(f'Length of the colors tuple is: {length_of_colors}')

# Add the number 4 to the numbers set.
numbers.add(4)
# Create a new key-value pair in the person dictionary (with new 'name' and age).
person['Sergiy'] = 18