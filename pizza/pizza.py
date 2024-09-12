from tabulate import tabulate
import sys
import os
import csv

def pinocho_menu(csvfile):
    try:
        with open(csvfile, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            print(tabulate(rows, headers="firstrow", tablefmt="grid"))
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

    pinocho_menu(filename)


if __name__ == "__main__":
    main()
