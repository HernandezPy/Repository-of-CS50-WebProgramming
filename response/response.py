import validators


def main():
    email = input("Enter your Email: ").strip()
    print(valid_email,(email))


def valid_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
