import csv

with open("before.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        before.append({"name": name, "home": house})


