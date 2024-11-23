
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
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
