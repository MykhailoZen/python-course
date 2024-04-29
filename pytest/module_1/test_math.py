import pytest


def adding(x, y):
    math = x + y
    return math

def test_assert():
    assert adding(1, 2) == 3

def test_assert_min():
    assert adding(1, -1) == 0

@pytest.mark.P0
def test_multiplication():
    assert 3 * 3 == 9
    assert 2 * 0 == 0

def test_multiplication_two():
    assert 2 * 1 == 2
    assert 5 * 3 == 15