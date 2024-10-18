import json

fruits = ['apple', 'banana', 'cherry', 'potato']
colors = ('blue', 'red', 'green')
numbers = set(range(1, 4))
person = {
    "Denys": 99
}

fruits.append("grape")

fruits.remove("potato")

for x in fruits:
    if "apple" in x:
        (print("Apple is present"))

print(len(colors))

numbers.add(4)
print(numbers)

person.update({"Denys2": 88})
print(json.dumps(person, indent=4, sort_keys=True))
