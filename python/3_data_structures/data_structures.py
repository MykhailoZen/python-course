# Homework_7

fruits = ['apple', 'banana', 'cherry', 'potato']

colors = ('green', 'orange', 'blue')

numbers = {1, 2, 3}

person = {
    'Mike': 33,
    'Dave': 45,
}

fruits.append('grape')

fruits.remove('potato')

# Another variant
fruits.pop(3)

print(fruits)
if 'apple' in fruits:
    print('Item is in the list')
else:
    print('There is no such element')

# Another variant
print("The number of apples in the list: ", fruits.count('apple'))

print("Tuple length: ", len(colors))

numbers.add(4)

print(numbers)

person['John'] = 25

print(person)