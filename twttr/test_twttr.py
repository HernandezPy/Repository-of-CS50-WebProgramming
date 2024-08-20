import pytest

from twttr import shorten


def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("APPLE") == "PPL"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_omitting_numbers():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("tw3tt3r") == "tw3tt3r"
    assert shorten("appl3") == "ppl3"



