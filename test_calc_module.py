import pytest
from calc_module import factorial, calculate_calories

def test_factorial_valid():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)

def test_calories_valid():
    assert calculate_calories(70, 1.2) == 2520.0

def test_calories_invalid():
    with pytest.raises(ValueError):
        calculate_calories(0, 1.2)
