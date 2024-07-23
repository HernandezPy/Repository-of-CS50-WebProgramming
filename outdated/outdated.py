import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def convert_date(date_str):
    numeric_date_pattern = re.compile(
        r"^(1[0-2]|[1-9])/([1-2][0-9]|3[0-1]|[1-9])/(\d{4})$"
    )
    named_date_pattern = re.compile(
        r"^(January|February|March|April|May|June|July|August|September|October|November|December) ([1-2][0-9]|3[0-1]|[1-9]), (\d{4})$"
    )


    numeric_match = numeric_date_pattern.match(date_str)
    if numeric_match:
        month, day, year = numeric_match.groups()
        return f"{year}-{int(month):02d}-{int(day):02d}"


    named_match = named_date_pattern.match(date_str)
    if named_match:
        month_name, day, year = named_match.groups()
        month = months.index(month_name) + 1
        return f"{year}-{month:02d}-{int(day):02d}"
    return None


def main():
    while True:
        date_str = input("Date: ").strip()
        converted_date = convert_date(date_str)
        if converted_date:
            print(converted_date)
            break
        else:
            pass


if __name__ == "__main__":
    main()
