def test_count_basic():
    assert count("hello, um, world.") == 1

def test_count_multiple():
    assert count("um um um") == 3

def test_count_mixed_case()
    assert count("Um, uM, UM") == 3

def test_count_no_um():
    assert count("hello world") == 0

def test_count_part_of_other_word():
    assert count("yummy") == 0

def test_count_punctuation():
    assert count("um...um?um!") == 3

def test_count_empty_string():
    assert count("") == 0
