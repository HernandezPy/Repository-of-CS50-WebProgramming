import pytest
from seasons import check_correct_date


def test_correct_date():
    assert check_correct_date("1995-02-14") == ("1995, 02, 14")
    assert check_correct_date("1995-2-14") == None


def test_incorrect_date():
    assert check_correct_date("November 5, 2014") == None
