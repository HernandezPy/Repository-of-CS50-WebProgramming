import pytest
from jar import jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(3)
    assert jar.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 9


def test_withdraw():
    jar = Jar()
    jar.withdraw(5)
    assert jar.size == 7
    jar.withdraw(1)
    assert jar.withdraw == 11



