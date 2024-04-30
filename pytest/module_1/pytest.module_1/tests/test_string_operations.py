# test_string_operations.py
import pytest

def is_palindrome(s):
    return s == s[::-1]

@pytest.mark.P0
def test_palindrome_positive_1():
    assert is_palindrome("stresseddesserts") == True

def test_palindrome_positive_2():
    assert is_palindrome("madam") == True

def test_palindrome_negative_3():
    assert is_palindrome("never") == False

@pytest.mark.P0
def test_palindrome_negative_4():
    assert is_palindrome("door") == False
