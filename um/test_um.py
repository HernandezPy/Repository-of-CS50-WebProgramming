def test_count_basic():
    assert count("hello, um, world.") == 1

def test_count_multiple():
    assert count("um um um") == 3

def test_count_mixed_case()
    assert count("Um, uM, UM") == 3

def test_count_no_um():
    # Test case where "um" does not appear at all
    assert count("hello world") == 0

def test_count_part_of_other_word():
    # Test case where "um" is part of another word
    assert count("yummy") == 0

def test_count_punctuation():
    # Test case with punctuation around "um"
    assert count("um...um?um!") == 3

def test_count_empty_string():
    # Test case with an empty string
    assert count("") == 0
