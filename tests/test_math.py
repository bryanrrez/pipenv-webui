import pytest
# from selenium import webdriver

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    diff = 1 - 1
    assert diff == 0

@pytest.mark.parametrize(
    'a, b, expected',
    [(1, 2, 2), (3, 5, 15), (-2, 0, 0), (-2, -6, 12), (-1, 1, -1)]
)
def test_multiplication(a, b, expected):
    assert a * b == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0