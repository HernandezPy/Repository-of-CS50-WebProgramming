from plates import is_valid

def test_is_valid_two_letters():
    assert is_valid("aad13") == True

def test_invalid_characters():
    assert is_valid("@dd14") == False

def test_correct_length():
    assert is_valid("douglas14") == False

def test_numbers_at_ends():
    assert is_valid("mmm123") == True
