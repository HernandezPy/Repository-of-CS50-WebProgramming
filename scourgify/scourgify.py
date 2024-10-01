import csv
import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename)
        sys.exit("file not found")

with open("before.csv", "r") as file:
    reader = file.read()
    print(reader)




