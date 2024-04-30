# test_math.py
from calculator import Calculator
import pytest

@pytest.mark.P0
def test_addition():
    calc = Calculator()
    assert calc.add(2, 7) == 9

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(6, 2) == 4

@pytest.mark.P0
def test_multiplication():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15

def test_division():
    calc = Calculator()
    assert calc.divide(15, 3) == 5

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)