# outdated.py
import re

# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def convert_date(date_str):
    # Regular expressions for matching date formats
    numeric_date_pattern = re.compile(r"^(1[0-2]|[1-9])/([1-2][0-9]|3[0-1]|[1-9])/(\d{4})$")
    named_date_pattern = re.compile(r"^(January|February|March|April|May|June|July|August|September|October|November|December) ([1-2][0-9]|3[0-1]|[1-9]), (\d{4})$")

    # Check if the input matches numeric date pattern
    numeric_match = numeric_date_pattern.match(date_str)
    if numeric_match:
        month, day, year = numeric_match.groups()
        return f"{year}-{int(month):02d}-{int(day):02d}"

    # Check if the input matches named date pattern
    named_match = named_date_pattern.match(date_str)
    if named_match:
        month_name, day, year = named_match.groups()
        month = months.index(month_name) + 1
        return f"{year}-{month:02d}-{int(day):02d}"

    # If the input doesn't match any pattern, return None
    return None

def main():
    while True:
        date_str = input("Date: ").strip()
        converted_date = convert_date(date_str)
        if converted_date:
            print(converted_date)
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
