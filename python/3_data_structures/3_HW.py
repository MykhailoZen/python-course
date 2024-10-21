fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ('blue', 'yellow', 'black')
numbers = {1, 2, 3}
person = {
    'Lukasz': 25,
    'Dasha': 18
}

fruits.append('grape')

fruits.remove('potato')

if 'apple' in fruits:
    print ("Apple is in the fruits list")
else: print ("Apple isn't in the fruits list")

print (f"Colours tuple has {len(colors)} items")

numbers.add(4)

person['Alex'] = 27
