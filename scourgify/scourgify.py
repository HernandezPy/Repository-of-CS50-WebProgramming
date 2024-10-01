import csv

def main():
    with open("before.csv", "r") as before, open("after.csv", "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["FirstName", "LastName", "House"])
        writer.writeheader()

        for row in reader:
            writer.writerow(
                {
                    "FirstName": row["FirstName, [2]"],
                    "LastName": row["LastName, [1]"],
                    "House": row["House, [4]"]
                }
            )


main()
