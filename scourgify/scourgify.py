import csv
import sys
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename)
        sys.exit("file not found")





