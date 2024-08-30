import pytest
from fuel import convert, gauge

def test_right_fractions():
    assert gauge(convert("E")) == "0/1"
    assert gauge(convert("25%")) == "1/4"
    assert gauge(convert("50%")) == "1/2"
    assert gauge(convert("75%")) == "3/4"
    assert gauge(convert("F")) == "4/4"

def test_error_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

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
