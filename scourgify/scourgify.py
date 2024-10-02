import csv

with open("before.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


