import pytest
from working import convert


def test_correct_time():
    assert convert("9:00 AM to 5:00 PM") == ("09:00 to 17:00")
    assert convert("7:00 AM to 3:00 PM") == ("07:00 to 15:00")
    assert convert("11:00 AM to 11:00 PM") == ("11:00 to 23:00")


def lower_case_time():
    assert convert("9:00 am to 5:00 pm") == ("09:00 to 17:00")


def incorrect_time():
    assert convert("09:00 AM to )
