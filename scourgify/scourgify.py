import csv

rows = []

with open("before.csv") as file:
    for row in file:
        name, house = row.rstrip()
        row = {"name": name, "house": house}
        rows.append(row)

for row in sorted(rows):
    print(f"{row['name'], row['hose']}")



