#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
#Create a tuple named colors with three colors of your choice.
#Create a set named numbers with the numbers from 1 to 3.
#Create a dictionary named person with the following key-value pairs: 'name' and age.

fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ('blue', 'red', 'green')
numbers = {1, 2, 3}
person = {
    "Denys": 99
}

#Add 'grape' to the fruits list.
fruits.append("grape")

#Remove 'potato' from the fruits list.
fruits.remove("potato")

#Check if 'apple' is in the fruits list and output the result.
for x in fruits:
    if "apple" in x:
        (print("Apple is present"))

#Calculate the length of the colors tuple and output it.
print(len(colors))

#Add the number 4 to the numbers set.
numbers.add(4)
print(numbers)

#Create a new key-value pair in the person dictionary (with new 'name' and age).
person.update({"Denys2": 88})
print(person)
