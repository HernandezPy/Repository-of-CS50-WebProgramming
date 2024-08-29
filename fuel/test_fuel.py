import pytest
from fuel import convert, gauge

def test_right_fractions():
    assert convert, gauge("0/1") == 0
    assert convert, gauge("1/4") == 25.0
    assert convert, gauge("1/2") == 50.0
    assert convert, gauge("3/4") == 75.0
    assert convert, gauge("4/4") == 100.0

def test_error_zero():_
    with pytest.raises(ZeroDivisionError):
        convert, gauge("1/0")

def test_error():
    with pytest.raises(ValueError):
        convert, gauge("5/3")

def test_invalid_fraction():
    with pytest.raises(ValueError):
        convert, gauge("200/3")
    with pytest.raises(ValueError):
        convert, gauge("a/b")
    with pytest.raises(ValueError):
        convert, gauge("1/one")
    with pytest.raises(ValueError):
        convert, gauge("1/2/3")
    with pytest.raises(ValueError):
        convert, gauge("3/-2")
