import pytest


def palindrome(word: str) -> bool:
    """
    Function check if input word is equal to its reversed version (palindrome)
    :param word: string type input
    :return: boolean if 2 forms of word are equal
    """

    if word == word[::-1]:
        return True
    else:
        return False


# For testing all cases from file - use cmd "pytest test_string_operations.py"
# For testing marked cases from file - use cmd 'pytest test_string_operations.py -m "palindrome"'
def test_true_palindrome():
    assert palindrome("madam")

@pytest.mark.palindrome
def test_capitilized_first_last_letters():
    assert palindrome("MadaM")


def test_empty_str():
    assert palindrome("madaM") == False


def test_type_input():
    with pytest.raises(TypeError):
        assert palindrome(11111)
