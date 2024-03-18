from functools import reduce
#Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.
list_to_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 100]
squared_list = list(map(lambda x: x ** 3,list_to_square))
print(squared_list)

#Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
even_list = list(filter(lambda x: x%2 == 0,list_to_square))
print(even_list)

#Write a function that calculates the factorial of a number using the functional approach.
def fibonacchi(n, baza={}):
    if n in baza:
        return baza[n]
    if n == 0:
        return 0
    elif (n == 1) | (n == 2):
        return 1
    else:
        baza[n] = fibonacchi(n-1, baza) + fibonacchi(n-2, baza)
        return baza[n]

print(fibonacchi(10))

# There is one more solution that I don't understand how it works, but I would like to understand it:

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib(11))

#Capitalize the first letter of each word in a sentence "hello world, how are you?".
string_to_cap = "hello world, how are you?"

def capitalize_first_letter(input):
    return input.title()

def capitalize_first_letter_func(sentence):
    return ' '.join(map(str.capitalize, sentence.split()))

print(capitalize_first_letter((string_to_cap)))
print(capitalize_first_letter_func(string_to_cap))

#Actually I couldn't solve it, had to use chatgpt


#Given a list of students and their marks as tuples:
#scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
#Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

def average_result(input):
    sum = 0
    for i in input:
        sum = sum + i[1]
    return sum/len(scores)

print(average_result(scores))