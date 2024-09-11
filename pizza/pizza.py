from tabulate import tabulate
import sys

def pinocho_menu(filename):
    try:
        with open(filename.csv, "r") as csvfile:
            reader = filename.DictReader(csvfile)
    except FileNotFoundError:
        sys.exit("File not Found")


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file"))
