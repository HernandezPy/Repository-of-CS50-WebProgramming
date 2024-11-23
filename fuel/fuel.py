
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            x, y = int(x, y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percentage = x / y * 100
            return percentage
        except (ValueError, ZeroDivisionError, TypeError):
            raise

def gauge(percentage):
       try:
           if percentage <= 1:
              return "E"
           elif percentage >= 99:
              return "F"
           else:
              return f'{round(percentage)}%'
       except (ValueError, ZeroDivisionError):
           raise


if __name__ == '__main__':
    main()
