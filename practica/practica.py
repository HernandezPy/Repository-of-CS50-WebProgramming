print("Bienvenido a nuestro verificador en linia")

age = int(input("Enter your age: "))
has_license = input("Do you have license? [Y/N]: ")

if has_license.lower() == "y/n":
    has_license = True
else:
    has_license = False

salary = int(input("Enter your salary: "))
if age <= 35:
    print("Your age it's okey")
    if has_license:
        print("Valid license")
        if salary >= 3500:
            print("Perfect! you're eligible")
        else:
            print("You are not eligible")
    else:
        print("Sorry, you need a valid license")
else:
    print("You are over our age limit")
