from fuel import get_fuel_fraction

def test_error_zero():
    with pytest.raise(ZeroDivisionError):
        get_fuel_fraction("0")

def test_error():
    with pytest.raise(ValueError):
        get_fuel_fraction(")

