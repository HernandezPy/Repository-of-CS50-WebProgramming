import csv


with open("before.csv", "w") as file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in fieldnames:
        last_name, first_name = row["name"].split(", ")
        writer.writerow({"first": first_name, "last": last_name, "house": row["house"]})

