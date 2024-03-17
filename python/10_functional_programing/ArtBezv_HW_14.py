#Task 1
numbers = [34, 27, 16, 76, 53, 28, 61, 29, 12]

def EvenNum(nums):
    if nums % 2 == 0:
        return nums

even_numbers = list(filter(EvenNum, numbers))
print(even_numbers)




#Task 2
def SquareNum(nums2):
    """
    Returns a new list containing squared numbers from the input list.
    """
    return list(map(lambda x: x ** 2, nums2))

numbers2 = [4, 5, 6, 7, 8, 9, 10, 11, 12]
squared_numbers = SquareNum
print(squared_numbers(numbers2))

#Optional
#Task 1

def factorial(n):
    if n == 0 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 6
print("Factorial of", number, "is", factorial(number))

#Task 2

def CapitilizeWord(word):
    return word.capitalize()

def CapitalizeSentence(sentence):
    words = sentence.split()

    capitalized_words = map(CapitilizeWord, words)
    return ' '.join(capitalized_words)

sentence = "hello world, how are you?"
capitalized_sentence = CapitalizeSentence(sentence)

print(capitalized_sentence)

sentence = "hello world, how are you?"

