import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50.0
    assert convert("3/4") == 75.0
    assert convert("1/4") == 25.0
    assert convert("0/1") == 0.0
    assert convert("4/4") == 100.0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

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

def test_gauge():
    assert gauge(0.0) == "E"
    assert gauge(1.0) == "E"
    assert gauge(50.0) == "50%"
    assert gauge(75.0) == "75%"
    assert gauge(100.0) == "F"


