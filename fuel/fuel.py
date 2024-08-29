def get_fuel_fraction(fraction):
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percentage = (x / y) * 100
            return percentage
        except (ValueError, ZeroDivisionError):
            raise


def main():
    while True:
        try:
             fraction = input("Fraction: ")
             percentage = get_fuel_fraction(fraction)
             if percentge <= 1:
                  print("E")
             elif percentage >= 99:
                  print("F")
             else:
                  print(f"{round(percentage)}%")
             break
        except (ValueError, ZeroDivisionError):
             pass


if __name__ == '__main__':
    main()
