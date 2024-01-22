#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']

#Create a tuple named colors with three colors of your choice.
colors = ('red', 'green', 'orange')

#Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}

#Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "name": "ale",
    "age": 6
}

#Add 'grape' to the fruits list.
fruits.append('grape')
print(fruits)

#Remove 'potato' from the fruits list.
fruits.remove('potato')
print(fruits)

#Check if 'apple' is in the fruits list and output the result.
for x in fruits:
    if x == 'apple':
        print ("apple is in the list")

#Calculate the length of the colors tuple and output it.
for y in colors:
    print(len(y))

#Add the number 4 to the numbers set.
numbers.add(4)
print(numbers)

#Create a new key-value pair in the person dictionary (with new 'name' and age).
print(person)
person["name"] = "noone"
person["age"] = 14
print(person)