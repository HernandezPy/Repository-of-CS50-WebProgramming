import pytest
from bank import value

def test_value_greeting():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("goodmorning") == 100

def test_value_startsWith_h():
    assert value("how are you") == 20
    assert value("how's it going") == 20
    assert value("have you been?") == 20

def test_value_no_h():
    assert value("Good morning") == 100
    assert value("What's up") == 100
    assert value("welcome") == 100

def test_value_case_insensitivity():
    

