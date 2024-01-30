# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
print(fruits)

# Create a tuple named colors with three colors of your choice.
colors = ('red', 'green', 'blue')
print(colors)

# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
print(numbers)

# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "Anton": 33,
    "Dmytro": 32,
    "Maksym": 40
}
print(person)

# Add 'grape' to the fruits list.
fruits.append('grape')
print(fruits)

# Remove 'potato' from the fruits list.
fruits.remove('potato')
print(fruits)

# Check if 'apple' is in the fruits list and output the result.
fruit = "apple"
if fruit in fruits:
    print(f'{fruit} is in the fruits list.')
else:
    print(f'{fruit} isn\'t in the fruits list.')

# Calculate the length of the colors tuple and output it.
calculate = len(colors)
print(f'The length of the colors is: {calculate}')

# Add the number 4 to the numbers set.
numbers.add(4)
print(numbers)

# Create a new key-value pair in the person dictionary (with new 'name' and age).
person['Irina'] = 62
print(person)
