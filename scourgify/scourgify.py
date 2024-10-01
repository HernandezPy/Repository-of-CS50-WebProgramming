import csv

def main():
    with open("before.csv", "r") as before, open("after.csv", "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["FirstName", "LastName", "House"])
        writer.writeheader()

        for row in reader:
            writer.writerow(
                {
                    "FirstName": row("name", [1]),
                    "LastName": row("name", [0]),
                    "House": row("house", [0])
                }
            )


main()
