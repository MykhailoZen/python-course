# Create a list named fruits with the following items: 'apple', 'banana', 'cherry', 'potato'.
fruits = ["apple", "banana", "cherry", "potato"]
print(fruits)

# Create a tuple named colors with three colors of your choice.
colors = ("blue", "yellow", "white")
print(colors)

# Create a set named numbers with the numbers from 1 to 3.
numbers = {1, 2, 3}
print(numbers)

# Create a dictionary named person with the following key-value pairs: 'name' and age.
person = {
    "name":  "Kate",
    "age":  33
}
print(person)

# Add 'grape' to the fruits list.
fruits.insert(4, "grape")
print(fruits)

# Remove 'potato' from the fruits list.
fruits.remove("potato")
print(fruits)

# Check if 'apple' is in the fruits list and output the result.
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list.")
else:
    print("No, 'apple' is not in the fruits list.")

# Calculate the length of the colors tuple and output it.
print("Number of colors:", len(colors))

# Add the number 4 to the numbers set.
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

# Create a new key-value pair in the person dictionary (with new 'name' and age).
person["new_name"] = "Katherine" #adding new name value
person["new_age"] = 34 #adding new age value
print(person)