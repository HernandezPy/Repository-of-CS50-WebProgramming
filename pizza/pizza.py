from tabulate import tabulate
import sys

def pinocho_menu(name):
    try:
        with open(name.csv, "r") as csvfile:
            reader = csv.DictReader(csvfile)
    except FileNotFoundError:
        sys.exit("Not a CSV file")
