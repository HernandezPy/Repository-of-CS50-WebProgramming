from seasons import check_correct_date

def main():
    test_check_correct_date

def correct_date():
    assert check_correct_date("1995-02-14") == ("1995, 02, 14")
    assert check_correct_date("1995-2-14") == None
    assert check_correct_date("November 5, 2014") == None

if __name__ == "__main__":
    main()
