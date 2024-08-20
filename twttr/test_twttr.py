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
