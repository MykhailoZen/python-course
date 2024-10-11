#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']

#Create a tuple named colors with three colors of your choice.
colors = ('red', 'green', 'yellow')

#Create a set named numbers with the numbers from 1 to 3.
numbers = {1,2,3}

#Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "Tom": 16,
    "Sam": 18,
    "Jerry": 19,
}
#Add 'grape' to the fruits list.
fruits.append('grape')

#Remove 'potato' from the fruits list.
fruits.remove('potato')

#Check if 'apple' is in the fruits list and output the result.
print('apple' in fruits)

#Calculate the length of the colors tuple and output it.
print(len(colors))

#Add the number 4 to the numbers set.
numbers.add(4)
print(numbers)

#Create a new key-value pair in the person dictionary (with new 'name' and age).
person["Mary"] = 21
print(person)