
#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
#Create a tuple named colors with three colors of your choice.
#Create a set named numbers with the numbers from 1 to 3.
#Create a dictionary named person with the following key-value pairs: 'name' and age.


fruits = ["apple", "banana", "cherry", "potato"]
colors = ("blue", "white", "red")
numbers = {1, 2, 3}
person = {"Lukasz": 40}

#Add 'grape' to the fruits list.
#Remove 'potato' from the fruits list.

fruits.append("grape")
fruits.remove("potato")

#Check if 'apple' is in the fruits list and output the result.

print("Apple in fruits:", "apple" in fruits)

#Calculate the length of the colors tuple and output it.

print("The number of colors is:", len(colors))

#Add the number 4 to the numbers set.
#Create a new key-value pair in the person dictionary (with new 'name' and age).

numbers.add(4)
person.update({"Daria": 35})
