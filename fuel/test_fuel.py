from fuel import get_fuel_fraction

def test_right_fractions():
    assert get_fuel_fraction("0/1") == E
    assert get_fuel_fraction("1/4") == 25.0
    assert get_fuel_fraction("1/2") == 50.0
    assert get_fuel_fraction("3/4") == 75.0
    assert get_fuel_fraction("4/4") == F

def test_error_zero():
    assert get_fuel_fraction("0/0") == "ZeroDivionError"

def test_error():
    assert get_fuel_fraction("200/3") == "ValueError"

