numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))


def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


print("Squared List:", square_numbers(numbers))
print("Even Numbers List:", even_numbers(numbers))
