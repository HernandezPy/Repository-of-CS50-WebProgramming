from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = check_correct_date(birthday)
    except TypeError:
        sys.exit("Invalid date")
    birth = date(int(year), int(month), int(day))
    today = date.today()
    difference = today - birth
    minutes_calculation = difference.days * 24 * 60
    words = p.number_to_words(minutes_calculation, andword="")
    print(words.capitalize() + " minutes")


def check_correct_date(birthday):
    try:
        if re.search(r"^\d{4}-\d{2}-\d{2}$", birthday):
            year, month, day = birthday.split("-")
            return year, month, day
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()

