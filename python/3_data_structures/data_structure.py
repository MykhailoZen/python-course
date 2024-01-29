# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
# Create a tuple named colors with three colors of your choice.
colors = ('red', 'black', 'blue')
# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    'Kate': 27,
    'Olya': 25,
    'Dima': 10,
    'Bohdan': 12
}
# Add 'grape' to the fruits list.
fruits.append('grape')
# Remove 'potato' from the fruits list.
fruits.remove('potato')
# Check if 'apple' is in the fruits list and output the result.
apple = "apple"
if apple in fruits:
    print(f'{apple} is in fruits')
else:
    print(f'{apple} is not in fruits')
# Calculate the length of the colors tuple and output it.
lens_of_colors = len(colors)
print(f'lens of colors is {lens_of_colors}')
# Add the number 4 to the numbers set.
numbers.add(4)
# Create a new key-value pair in the person dictionary (with new 'name' and age).
person['Luba'] = 45
print(person)
