import pytest
from bank import value

def test_value_greeting():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("goodmorning") == 100
