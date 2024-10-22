import re


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if not match:
        return False

    for part in match.groups():
        if not 0 <= int(part) <= 255:
            return False
    return True


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
