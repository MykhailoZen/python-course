
#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato':
fruits = ['apple', 'banana', 'cherry', 'potato']

#Create a tuple named colors with three colors of your choice:
colors = ('red', 'yellow', 'green')

#Create a set named numbers with the numbers from 1 to 3:
numbers = {1, 2, 3}

#Create a dictionary named person with the following key-value pairs: 'name' and age:
person = {'name': 'Vlad', 'age': 10}

#Add 'grape' to the fruits list:
add_grape = fruits + ['grape']
print('List with grape:', add_grape)

#Remove 'potato' from the fruits list:
del fruits[3]
print('List without potato: ', fruits)

#Check if 'apple' is in the fruits list and output the result:
if_apple_in_fruits = 'apple' in fruits
print('If apple is in the fruits list? ', if_apple_in_fruits)

#Calculate the length of the colors tuple and output it:
print('Calculated length of the colors: ', len(colors))

#Add the number 4 to the numbers set:
add_4 = numbers | {4}
print('Add the number 4 to the numbers: ', add_4)

#Create a new key-value pair in the person dictionary (with new 'name' and age):
person['new_name'] = 'Tom'
person['new_age'] = 20
print('New key-value pair: ', person)