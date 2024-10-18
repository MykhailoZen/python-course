import functools

# Given a list of numbers, write a list comprehension that produces a copy of the list.
numbers = [1,2,3,4,5,6,7,8,9,10,11]
new_numbers = [number for number in numbers]

# Given a list of numbers (e.g. range(1, 11)), write a list comprehension that produces a list of only the even numbers.
even_numbers = [number for number in numbers if number%2 ==0]

# Solve the task above using filter() with a lambda function.
filtered_numbers = list(filter(lambda x: x%2 == 0, numbers))

# Given the list [("apple", 50), ("banana", 10), ("cherry", 30)], sort it by the number using the lambda function.
fruits = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_fruits = list(sorted(fruits, key = lambda x: x[1]))
print(sorted_fruits)

# Given the list [1, 2, 3, 4, 5], calculate the multiplication result of all values using functools.reduce()
# from the standard library and a lambda function.
lis = [1,2,3,4,5]
print(functools.reduce(lambda x, y: x * y, lis))

#Given a list of lists (e.g. [[5, 4, 7], [8, 9, 6], [7, 2, 4]]),
# write a list comprehension that produces a single list of all items (e.g. [5, 4, 7, 8, 9, 6, 7, 2, 4]).
list1 = [[5, 4, 7], [8, 9, 6], [7, 2, 4]]
def extract(any_list):
    new_list = []
    for i in any_list:
        for n in i:
            new_list.append(n)
    return new_list

list2 = [n for i in list1 for n in i]

print(extract(list1))
print(list2)


#Using a dict comprehension flip the dictionary (make keys from values and vice versa).
# For example: {'a': 1, 'b': 2, 'c': 3} -> {1: 'a', 2: 'b', 3: 'c'}.
collection = {'a': 1, 'b': 2, 'c': 3}
new_collection = {number:letter for (letter, number) in collection.items()}
print(new_collection)






