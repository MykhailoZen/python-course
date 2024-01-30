#Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']

#Create a tuple named colors with three colors of your choice.
colors = ("red", "blue", "white")

#Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}

#Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "Noname":99
}

#Add 'grape' to the fruits list.
fruits.append('grape')

#Remove 'potato' from the fruits list.
fruits.remove('potato')

#check if apple in fruits list
x = 'apple' 
if x in fruits:
    print ('Yes, apple in fruits list')
else: 
    print ('No')

#Calculate the length of the colors tuple and output it.
print (len(colors))

#Add the number 4 to the numbers set.
numbers.add(4)

#Create a new key-value pair in the person dictionary (with new 'name' and age).
person.update({"Mark": 55})

#for checking output
print ('Upd fruits list:', fruits)
print ('Upd colors tuple:', colors)
print ('Upd nambers set:', numbers)
print ('Upd person dictionary:', person)