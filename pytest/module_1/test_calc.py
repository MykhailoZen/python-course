import pytest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide to 0")
        return x / y

class TestCalculator(Calculator):

    def test_add(self):
        assert self.add(2, 3) == 5

    def test_subtract(self):
        assert self.subtract(4,3) == 1

    def test_multply(self):
        assert self.multiply(2, 4) == 8

    def test_divide(self):
        calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            calc.divide(3, 0)

