import pytest
from quick_calc import core

def test_add_basic():
    assert core.add(5, 3) == 8

def test_subtract_basic():
    assert core.subtract(10, 4) == 6

def test_multiply_basic():
    assert core.multiply(6, 7) == 42

def test_divide_basic():
    assert core.divide(20, 5) == 4

# Edge cases
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        core.divide(10, 0)

def test_negative_numbers():
    assert core.add(-2, -3) == -5
    assert core.subtract(-10, -4) == -6

def test_decimal_numbers():
    assert core.multiply(2.5, 4) == 10.0
    assert core.divide(1, 4) == 0.25

def test_large_numbers():
    assert core.add(10**12, 10**12) == 2 * 10**12