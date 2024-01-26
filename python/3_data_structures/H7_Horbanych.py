fruits = ['apple', 'banana', 'Mango', 'potato']
colors = ('red', 'yellow', 'green')
numbers = {1, 2, 3}
person = {'name': 'Bohdan', 'age': 28}
fruits.append('grape')
fruits.remove('potato')
print('Is apple in the fruits list?', 'apple' in fruits)
print('Length of the colors tuple:', len(colors))


numbers.add(4)

person['new_name'] = 'Alex'
person['new_age'] = 90

print('Updated fruits list:', fruits)
print('Updated colors tuple:', colors)
print('Updated numbers set:', numbers)
print('Updated person dictionary:', person)
