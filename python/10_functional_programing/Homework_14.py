from functools import reduce

def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))


def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))


def capitalize_sentence(sentence):
    return sentence.title()


def average_score(scores):
    scores_only = map(lambda x: x[1], scores)
    total_score = sum(scores_only)
    return total_score / len(scores) if scores else 0


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(square_numbers(numbers))

    print(filter_even_numbers(numbers))

    print(factorial(5))

    sentence = "hello world, how are you?"
    print(capitalize_sentence(sentence))

    scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
    print(average_score(scores))
