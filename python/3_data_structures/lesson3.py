fruits = ['apple', 'banana', 'cherry', 'potato']
colours = ('black', 'blue', 'yellow')
numbers = {1, 2, 3}
person= {
    "Dmytro" : 32
}
#Actions for fruits
fruits.append("grape")
fruits.remove("potato")
print("apple" in fruits)

#Action for colours
print(len(colours))

#Action for numbers
numbers.add(4)
print(numbers)

#Actions for person
person.update({"Daria": 35})
print(person)
