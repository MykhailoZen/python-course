fruits = ['apple', 'banana', 'cherry', 'potato']
print(f"Original fruit list: {fruits}")
fruits.append('grape')
fruits.remove('potato')
print(f"Modified fruit list: {fruits}")
check = 'apple' in fruits
print ("Apple is in fruits list: " + str(check))
print("----------")

colors = ('red', 'white', 'black')
print(colors)
length = len(colors)
print (f"The length of the colors tuple is: {length}")
print("----------")

numbers = {1, 2, 3}
numbers.add(4)
print (numbers)
print("----------")

person = {'name': 'Serhii', 'age': 64}
person.update({'name2': 'Vlad', 'age2': 54})
for key in person:
    print (person[key])

