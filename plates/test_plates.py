from plates import is_valid

def test_number_placement():
    assert is_valid("aad13") == True

def test_invalid_characters():
    assert is_valid("@dd14") == False

def test_beginning_alphabetical():
    assert is_valid("aei") == True

def test_numbers_at_ends():
    assert is_valid("mmm123") == True
