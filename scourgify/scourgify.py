import csv
import sys

def main()"
    if len(sys.argv) != 2:
        sys.exit("Too few commnand-lines arguments)


with open("before.csv", "r") as file:
    for row in file:
        print(row.rstrip())
