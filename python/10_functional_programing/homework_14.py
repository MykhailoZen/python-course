# Write a function that takes a list of numbers as input and returns a new list containing the square of each number
def my_func(nums):
    return [num ** 2 for num in nums]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_func(numbers))


# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
def is_even(x):
    return list(filter(lambda num: num % 2 == 0, x))


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(is_even(nums_list))


# Write a function that calculates the factorial of a number using the functional approach.
def factorial(x):
    from math import factorial
    return factorial(x)


print(factorial(5))

# Capitalize the first letter of each word in a sentence
sentence = "hello world, how are you?"
capitalized_sentence = sentence.title()
print(capitalized_sentence)
