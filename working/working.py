import re


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", re.IGNORECASE
    match = re.match(pattern, s)

    if not match:
        raise ValueError("ValueError")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    if not (1 <= start_hour <= 12) or not (0 <= start_minute < 60):
        raise ValueError("ValueError")
    if not (1 <= end_hour <= 23) or not (0 <= end_minute < 60):
        raise ValueError("ValueError")

    def to_24_hour(hour, minute, period):
        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0
        return f"{hour:02}:{minute:02}"

    start_24 = to_24_hour(start_hour, start_minute, start_period)
    end_24 = to_24_hour(end_hour, end_minute, end_period)
    return f"{start_24} to {end_24}"


if __name__ == "__main__":
    try:
        print("Enter working hours (e.g., '9:00 AM to 5:00 PM'")
        time = input("HOUR: ")
        print(convert(time))
    except ValueError as e:
        print(e)
