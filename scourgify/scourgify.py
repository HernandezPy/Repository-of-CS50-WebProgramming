import csv
import sys
import os

def correct_file():
    with open("before.csv", "r") as before, open("after.csv", "w", newline='') as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["FirstName", "LastName", "House"])
        writer.writeheader()

        for row in reader:
            last_name, first_name = row["name"].split(", ")
            writer.writerow(
                {
                    "FirstName": first_name,
                    "LastName": last_name,
                    "House": row["house"]
                }
            )


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many commnad-line arguments")
    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    correct_file()

if __name__ == "__main__":
    main()
