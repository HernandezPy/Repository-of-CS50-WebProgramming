import pytest

from twttr import shorten

def test_vowels():
    assert(vowels) == ['a', 'e', 'i', 'o', 'u']


def text_shorten():
    assert(shorten) == [char for char in word if char.lower() not in vowels]
