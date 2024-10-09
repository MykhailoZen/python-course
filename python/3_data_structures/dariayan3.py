fruits = ['apple', 'banana', 'cherry', 'potato']
color = ('red','yellow','orange','green','blue')
numbers = {1,2,3}
persons = {'Daria': 23}

print(f"Fruits: {fruits}")
print(f"Colors: {color}")
print(f"Numbers: {numbers}")
print(f"Persons: {persons}")

print('Add grape to Fruits.')
fruits.append('grape')
print(f"Fruits: {fruits}")

print('Remove potato from Fruits.')
fruits.remove('potato')
print(f"Fruits: {fruits}")

print(f"Are \'apple\' in fruits? - {'apple' in fruits}")

print(f"Length of Color tuple: {len(color)}")

print('Add 4 to numbers.')
numbers.add(4)
print(f"Numbers: {numbers}")

print('Add Mariia to Persons.')
persons.update({'Mariia':8})
print(f"Persons: {persons}")










