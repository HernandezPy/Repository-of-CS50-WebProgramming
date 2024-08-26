def main():
    return (
        starts_with_two_letters(s) and
        correct_lengt(s) and
        numbers_at_
    )


def is_valid(s):
    return (
    starts_with_two_letters(s) and
    correct_length(s) and
    numbers_at_end(s) and
    no_invalid_characters(s)
   )
def starts_with_two_letters(s):
    return len(s) >= 2 and s[:2].isalpha()


def correct_length(s):
    return 2 <= len(s) <= 6

def numbers_at_end(s):
    has_number = False
    for char in s:
        if char.isdigit():
            if char == '0' and not has_number:
                return False
            has_number = True
        elif has_number:
            return False
    return True


def no_invalid_characters(s):
    return s.isalnum()


if __name__ == '__main__':
 main()
