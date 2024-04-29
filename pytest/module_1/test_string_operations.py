import unittest

import pytest


def polindrome(p):
    return p == p[::-1]

class TestStringOperations(unittest.TestCase):

    @pytest.mark.palindrome
    def test_posit_polindrome(self):
        self.assertTrue(polindrome("level"))

    def test_not_palindrome(self):
        self.assertFalse(polindrome("hello"))
        self.assertFalse(polindrome("world"))

    @pytest.mark.P0
    def test_polin_pos(self):
        assert polindrome("level")

    @pytest.mark.P0
    def test_polin_neg(self):
        assert not polindrome("world")
