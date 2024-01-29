fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ('blue', 'grey', 'white')
numbers = {1, 2, 3}
person = {'Conrad': 87, 'Patrick': 3, 'Jonathan': 31}

fruits.append('grape')
fruits.remove('potato')
for item in fruits:
    if item == 'apple':
        print("The apple is on the list!")
print("The length of the Colors tuple is %s" % (len(colors)))
numbers.add(4)
person.update({'Malcolm':13})
