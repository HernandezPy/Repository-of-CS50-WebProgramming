from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("aa123") == True
    assert is_valid("A") == False

def test_correct_length():
    assert is_valid("AB") == True
    assert is_valid("12345") == False

def test_no_invalid_characters():
    assert is_valid("ABC333") == True
    assert is_valid("AB 234") == False

def test_numbers_at_ends():
    assert is_valid("AB123") == True
    assert is_valid("AB12C3") == False

def test_is_valid():
    assert is_valid("ABC123") == True
    assert is_valid("AB") == True
    assert is_valid("AB12c3") == False
    assert is_valid("A12345") == False
    assert is_valid("AB12345") == False
    assert is_valid("AB@123") == False
