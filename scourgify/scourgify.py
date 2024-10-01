import csv

def main():
    with open("before.csv", "r") as before, open("after.csv", "w", newline='') as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["FirstName", "LastName", "House"])
        writer.writeheader()

        for row in reader:
            last_name, first_name = row["name"].split(", ")
            writer.writerow(
                {
                    "FirstName": firts_name,
                    "LastName": last_name,
                    "House": row["house"]
                }
            )


main()
