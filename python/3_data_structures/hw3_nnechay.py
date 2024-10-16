# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
# Create a tuple named colors with three colors of your choice.
# Create a set named numbers with the numbers from 1 to 3.
# Create a dictionary named person with the following key-value pairs: 'name' and age.
# Add 'grape' to the fruits list.
# Remove 'potato' from the fruits list.
# Check if 'apple' is in the fruits list and output the result.
# Calculate the length of the colors tuple and output it.
# Add the number 4 to the numbers set.
# Create a new key-value pair in the person dictionary (with new 'name' and age).

fruits = ['apple', 'banana', 'cherry', 'potato'] # list fruits creation

colors = ('red', 'blue', 'green') # tuple colors creation

numbers = {1, 2, 3} # set numbers creation

person = {'Nataliia' : 40} # dict person creation

"""Output of operations with the descriptions"""

# Add 'grape' to the fruits list.
def fruits_with_grape():
    updated_fruits = fruits.copy()
    updated_fruits.append('grape')
    print('The "fruits" list after I added the "grape" value to the original list is', updated_fruits)


# Remove 'potato' from the fruits list.
def fruits_without_potato():
     updated_fruits = fruits.copy()
     updated_fruits.remove('potato')
     print('The "fruits" list after I removed the "potato" value from the original list is', updated_fruits)

# Check if 'apple' is in the fruits list and output the result.
def apple_in_fruits():
    if 'apple' in fruits:
        print('Apple is in the fruits list')
    else:
        print('There is no Apple')

print('-------All actions with the list--------')
print('Original list is', fruits)
fruits_with_grape()
fruits_without_potato()
apple_in_fruits()

#
# Calculate the length of the colors tuple and output it.
#

print('-------Actions with the tuple-------')
print('The colors tulpe is', colors)
print('Number of elements in the colors tuple is', len(colors))

#
# Add the number 4 to the numbers set.
#

print('-------Actions with the set-------')
print('Original set is', numbers)
numbers.add(4)
print('The updated Set after I added 4 is', numbers)

#
# Create a new key-value pair in the person dictionary (with new 'name' and age).
#

print('-------Actions with the dictionary-------')
print('Original dictionary is', person)
person['Daniil'] = 15
print('Updated dictionary after I added new item is', person)
