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
            pass


def main():
    percentage = get_fuel_fraction()
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{round(percentage)}%')


if __name__ == '__main__':
    main()
