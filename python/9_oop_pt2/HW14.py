from functools import reduce

class NumberOperations:
    def square_numbers(self, numbers):
        """Returns a new list containing the square of each number."""
        return list(map(lambda x: x**2, numbers))

    def filter_even_numbers(self, numbers):
        """Returns a new list containing only the even numbers."""
        return list(filter(lambda x: x % 2 == 0, numbers))

    def factorial(self, n):
        """Calculates the factorial of a number."""
        return reduce(lambda x, y: x * y, range(1, n + 1), 1)

class StringOperations:
    def capitalize_sentence(self, sentence):
        """Capitalizes the first letter of each word in a sentence."""
        return ' '.join(map(str.capitalize, sentence.split()))

class StudentOperations:
    def average_score(self, scores):
        """Calculates the average score of the students."""
        total_score = sum(score[1] for score in scores)
        return total_score / len(scores)

# Given list of students and their marks
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]

# Test the functions
number_ops = NumberOperations()
string_ops = StringOperations()
student_ops = StudentOperations()

numbers = [1, 2, 3, 4, 5]
print("Squared Numbers:", number_ops.square_numbers(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even Numbers:", number_ops.filter_even_numbers(numbers))

n = 5
print("Factorial of", n, ":", number_ops.factorial(n))

sentence = "hello world, how are you?"
print("Capitalized Sentence:", string_ops.capitalize_sentence(sentence))

print("Average Score:", student_ops.average_score(scores))
