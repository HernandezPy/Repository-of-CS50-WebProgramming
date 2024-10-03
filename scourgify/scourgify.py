import csv

before = []

with open("before.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        print(name, house)
