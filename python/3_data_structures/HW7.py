#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
print(f"Original fruit list: {fruits}")
fruits.append('grape') #Add 'grape' to the fruits list.
fruits.remove('potato') #Remove 'potato' from the fruits list.
print(f"Modified fruit list: {fruits}")
check = 'apple' in fruits #Check if 'apple' is in the fruits list and output the result.
print ("Apple is in fruits list: " + str(check))

print("---------")

#Create a tuple named colors with three colors of your choice.
colors = ('red', 'white', 'black')
print(colors)
#Calculate the length of the colors tuple and output it.
length = len(colors)
print (f"The length of the colors tuple is: {length}")

print("---------")

#Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
numbers.add(4) #Add the number 4 to the numbers set.
print (numbers)

print("---------")

#Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {'name': 'Serhii', 'age': 64}
#Create a new key-value pair in the person dictionary (with new 'name' and age).
person.update({'name2': 'Vlad', 'age2': 54})
for key in person:
    print (person[key])

