fruits = ['apple', 'banana', 'cherry', 'potato'] #list
colors = ('purple', 'blue', 'octarine') #tuple
numbers = {1, 2, 3} #set
person = {'name': 'Yennefer', 'age': 93} #dictionary
fruits.append('grape') # add grape
fruits.remove('potato') # remove potato
print(fruits) # print list
if 'apple' in fruits:
    print('Yes, apple is in the fruits-list') # check if apple in fruits
print(f'The length is  {len(colors)}') # calculate and print length of colors
numbers.add(4) # add 4 to set
print(numbers) # print set
person2 = {'name': 'Jaskier', 'age': 'undefined'} #new key-value pair in the person
person.update(person2)
print(person)
