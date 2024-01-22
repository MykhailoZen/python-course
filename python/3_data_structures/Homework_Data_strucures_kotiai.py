# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
print('1. List named fruits: ')
fruits = ['apple', 'banana', 'cherry', 'potato']
print("fruits: %s" % (fruits))

# Create a tuple named colors with three colors of your choice.
print('2. Tuple named colors:')
colors = ('red', 'blue', 'green')
print(colors)

# Create a set named numbers with the numbers from 1 to 3.
print('3. Set named numbers: ')
numbers = {1, 2, 3}
print("numbers: %s" % (numbers))

# Create a dictionary named person with the following key-value pairs: 'name' and age.
print('4. Dictionary named person: ')
person = {'Yelisei': 32, 'Kalenyk': 30, 'Kuzma': 25}
print("person: %s" % (person))

# Add 'grape' to the fruits list.
print('5. Add "grape" to the fruits list: ')
fruits.append('grape')
print("Added 'grape' to the fruits list: %s" % (fruits))

# Remove 'potato' from the fruits list.
print('6. Remove "potato" from the fruits list ')
fruits.remove('potato')
print("Final fruits list %s" % (fruits))

# Check if 'apple' is in the fruits list and output the result.
print('7. Checking if "apple" is in the fruits list: ')
print("apple" in fruits)
print("The fruits set is %s" % (fruits))

# Calculate the length of the colors tuple and output it.
print('8. Calculate the length of the colors tuple: ')
print("The length is %s" % (len(colors)))

# Add the number 4 to the numbers set.
print('9. Add the number 4 to the numbers set ')
numbers.add(4)
print("The final numbers set is %s" % (numbers))

# Create a new key-value pair in the person dictionary (with new 'name' and age).
print('10. Create new key-value pair in the person dictionary')
new_key_value_pair = {'Petia': 28}
person.update(new_key_value_pair)
print("The final person dictionary is %s" % (person))
