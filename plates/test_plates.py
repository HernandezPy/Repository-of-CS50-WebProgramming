from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("aad13") == True

def test_zero_placement():
    assert is_valid("ddd140") == True

def test_beginning_alphabetical():
    assert is_valid("abc333") == True

def test_numbers_at_ends():
    assert is_valid("mmm123") == True

def test_alphanumeric_characters():
    assert is_valid("yes123")
