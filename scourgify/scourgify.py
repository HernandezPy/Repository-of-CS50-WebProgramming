import csv
import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few commnand-lines arguments)
                 
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does Not exist")


with open("before.csv", "r") as file:
    for row in file:
        print(row.rstrip())
