import pytest
from working import convert


def test_correct_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("7:00 AM to 3:00 PM") == "07:00 to 15:00"
    assert convert("11:00 AM to 11:00 PM") == "11:00 to 23:00"
    assert convert("6 AM to 6 PM") == "06:00 to 18:00"


def test_lower_case_time():
    assert convert("9:00 am to 5:00 pm") == "09:00 to 17:00"


def test_incorrect_time():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
    with pytest.raises(ValueError):
        convert("3:60 AM to 9:69 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("1:00 PM to 01:00 AM")


def test_omits_to():
    with pytest.raises(ValueError):
        convert("9:00 AM - 7:00 PM")
    with pytest.raises(ValueError):
        convert("8:00 _ 17:00")


def test_out_of_range():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:00 PM to 3:00 AM")
