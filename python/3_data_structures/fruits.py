fruits = ['apple', 'banana', 'cherry', 'potato']
colours = ('red', 'blue', 'green', 'yellow')
numbers = {1, 2, 3}
person = {'name': 'Viktor', 'age': 30}

fruits.append('grape')
fruits.remove('potato')

if 'apple' in fruits:
    print(fruits)

print(len(colours))

numbers.add(4)

person['project'] = ['DPD']

if len(colours) < 5:
    print(fruits)
    print(colours)
    print(numbers)
    print(person)
