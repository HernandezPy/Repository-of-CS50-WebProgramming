import csv


with open("before.csv" "w") as file:
    reader = csv.DictReader(file)
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        last_name, first_name = row["name"].split(", ")
        writer.writerow({"first": first_name, "last": last_name, "house": row["house"]})
        
