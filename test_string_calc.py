import pytest

from string_calc import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4,5") == 15

def test_negative_number_raises_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        add("1,-1")

def test_multiple_negative_numbers_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed -1,-2"):
        add("1,-1,-2")

def test_newline_as_delimiter():
    assert add("1\n2,3") == 6

def test_custom_single_char_delimiter():
    assert add("//;\n1;2") == 3

def test_custom_multi_char_delimiter():
    assert add("//[***]\n1***2***3") == 6

def test_multiple_custom_delimiters():
    assert add("//[*][%]\n1*2%3") == 6

def test_multiple_multi_char_delimiters():
    assert add("//[***][%%]\n1***2%%3") == 6