import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50.0 and gauge(50) == "50%"
    assert convert("3/4") == 75.0 and gauge(75) == "75%"
    assert convert("1/4") == 25.0 and gauge(25) == "25%"
    assert convert("4/4") == 100.0 and gauge(100) == "F"
    assert convert("0/1") == 0.0 and gauge(0) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_all_errors():
    with pytest.raises(ValueError):
        convert("2")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/one")
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("3/-2")



