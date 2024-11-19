from seasons import check_correct_date(birthday)
import pytest

def correct_date():
    assert check_correct_date("1995-02-14") == ("1995, 02, 14")
    assert check_correct_date("1995-2-14") == None
    assert check_correct_date("November 5, 2014") == None
