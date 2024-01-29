'''Practice
Make sure to perform these operations using the basic capabilities of the data structures
(without using comprehensions, lambdas, functions or other advanced features).
'''

# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ['apple', 'banana', 'cherry', 'potato']
print(type(fruits), fruits)

# Create a tuple named colors with three colors of your choice.
colors = ('red', 'green', 'blue')
print(type(colors), colors)

# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
print(type(numbers), numbers)

# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {'Bob': 19,
          'Alice': 20,
          'John' : 21}
print(type(person), person)

# Add 'grape' to the fruits list.
fruits.append('grape')
print(fruits)

# Remove 'potato' from the fruits list.
fruits.remove(fruits[3])
print(fruits)

# Check if 'apple' is in the fruits list and output the result.
needed_fruit = "apple"
if (needed_fruit in fruits):
    print(f"Yes, {needed_fruit} it's in the list")
else:
    print(f"Nope, {needed_fruit} is NOT in the list")

# Calculate the length of the colors tuple and output it.
print(len(colors))

# Add the number 4 to the numbers set.
numbers.add(4)
print(numbers)

# Create a new key-value pair in the person dictionary (with new 'name' and age).
person['Smith'] = 99
print(person)
