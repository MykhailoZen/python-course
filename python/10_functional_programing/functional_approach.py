from mako.testing.helpers import result_lines

lists=[1,2,3,4,5,6,7,8,9]


#1. Write a function that takes a list of numbers as input and returns a new list containing the square of each number using the functional approach.

def squaring(lists):
    return [num * num for num in lists]

def squaring2(lists):
    return list(map(lambda x: x*x, lists))

print(squaring(lists))
print(squaring2(lists))

#2. Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

def evenation(lists):
    return [number for number in lists if number % 2 == 0]

print(evenation(lists))

#3. Write a function that calculates the factorial of a number using the functional approach.

def factorial(number):
    result = 1
    for number in range(1,number+1):
        result = result*number
    return result

print(factorial(10))

#4. Capitalize the first letter of each word in a sentence "hello world, how are you?".

sentence = "hello world, how are you?"

def capitalizator(sentence):
    answer=[]
    for word in sentence.split():
        answer.append(word.capitalize())
    return " ".join(answer)

print(capitalizator(sentence))

#5. Given a list of students and their marks as tuples Write a function that calculates the average score of
# the students in the list. The function should take the list of tuples as input and return the average score.

scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

def averator(list):
    sum=0
    for record in scores:
        sum+=record[1]
    return sum/len(list)

print(averator(scores))
