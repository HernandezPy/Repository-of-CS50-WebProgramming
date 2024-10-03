import csv


with open("before.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
