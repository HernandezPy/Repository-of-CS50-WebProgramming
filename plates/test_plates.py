from plates import is_valid

def test_number_placement():
    assert is_valid("aad13") == True

def test_zero_placement():
    assert is_valid("ddd140") == True

def test_without_beginning_alphabetical():
    assert is_valid("132aaa") == False

def test_numbers_at_ends():
    assert is_valid("mmm123") == True

def test_alphanumeric_characters():
    assert is_valid("yes123")
