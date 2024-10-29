import pytest
from numb3rs import validate


def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("255.198.1.3") == True
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True


def test_no_validate():
    assert validate("300,300,200,333") == False
    assert validate("1:2:3:3") == False
    assert validate("cat") == False


def test_range():
    assert validate("260.3.23.12") == False
    assert validate("1.256.2.124") == False
    assert validate("23.122.300.0") == False
    assert validate("1.2.3.1000") == False
