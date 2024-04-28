import pytest
from module_1 import calculator


def adding(a, b):
    """Simple addition"""
    return a + b


@pytest.mark.P0
def test_adding():
    assert adding(2, 1) == 3


# Test name filtering - cmd 'pytest test_calculator.py -k "multiplication_apart"'
@pytest.mark.P0
def test_multiplication_apart():
    assert calculator.multiplication(2, 2) == 4


class TestCalculator:
    def test_addition(self):
        assert calculator.addition(2, 2) == 4
        assert calculator.addition(2, -2) == 0
        assert calculator.addition(0, 1e3) == 1e3

    def test_subtraction(self):
        assert calculator.subtraction(5, 5) == 0
        assert calculator.subtraction(10, -10) == 20
        assert calculator.subtraction(1e3, 1e2) == 900

    def test_multiplication(self):
        assert calculator.multiplication(2, 2) == 4
        assert calculator.multiplication(1, 2) == 2
        assert calculator.multiplication(-1, -5) == 5

    def test_division(self):
        assert calculator.division(1, 2)
        assert calculator.division(10, 2)
        with pytest.raises(ZeroDivisionError):
            assert calculator.division(5, 0)
