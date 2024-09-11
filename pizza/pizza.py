from tabulate import tabulate
import sys
import os

def pinocho_menu(filename):
    try:
        with open(filename, "r") as file:
            file = filename.reader(filename)
    except FileNotFoundError:
        sys.exit("File not Found")


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does Not exist")

    filename = pinocho_menu(filename)


if __name__ == "__main__":
    main()
