import functools


def square_nums(nums: list) -> list:
    """
    Function returns a new list containing the square of each number
    :param nums: list of numbers
    :return: list of squared numbers
    """
    return list(x ** 2 for x in nums)


numbers = [1, 2, 3, 4, 5]
print(square_nums(numbers))


def even_nums(nums: list) -> list:
    """
    Function returns a new list containing only the even numbers
    :param nums: list of numbers
    :return: list of even numbers
    """
    return list(filter(lambda num: num % 2 == 0, nums))


numbers1 = [1, 2, 3, 4, 5]
print(even_nums(numbers1))


def factorial(n: int) -> int:
    """
    Function calculates the factorial of a number
    :param n: input number
    :return: factorial of number
    """
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(5))


def diya_capitalize(words: str) -> str:
    """
    Function capitalizes the first letter of each word in a sentence
    :param words: input sentence
    :return: string with capitalized first letter in a sentence
    """
    return " ".join(list(word.capitalize() for word in words.split(" ")))


sentence = "hello world, how are you?"
print(diya_capitalize(sentence))


def average_scores(scores: list) -> int:
    """
    Function that calculates the average score of the students in the list
    :param scores: input list of students with scores
    :return: average score for students
    """
    return sum(map(lambda x: x[-1], scores)) / len(scores)


example = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
print(average_scores(example))
