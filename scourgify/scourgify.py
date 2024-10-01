import csv

def main():
    with open("before.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"])

main()
