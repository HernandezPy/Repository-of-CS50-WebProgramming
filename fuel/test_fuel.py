import pytest
from fuel import get_fuel_fraction

def test_right_fractions():
    assert get_fuel_fraction("0/1") == 0
    assert get_fuel_fraction("1/4") == 25.0
    assert get_fuel_fraction("1/2") == 50.0
    assert get_fuel_fraction("3/4") == 75.0
    assert get_fuel_fraction("4/4") == 100.0

def test_error_zero():
    with pytest.raises(ZeroDivisionError):
        get_fuel_fraction("1/0")

def test_error():
    with pytest.raises(ValueError):
        get_fuel_fraction("5/3")

def test_invalid_fraction():
    with pytest.raises(ValueError):
        get_fuel_fraction("200/3")
    with pytest.raises(ValueError):
        get_fuel_fraction("a/b")
    with pytest.raises(ValueError):
        get_fuel_fraction("1/one")
    with pytest.raises(ValueError):
        get_fuel_fraction("1/2/3")
    with pytest.raises(ValueError):
        get_fuel_fraction("3/-2")
