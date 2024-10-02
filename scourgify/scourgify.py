with open("before.csv") as file:
    for row in file:
        row = row.rstrip().split(",")
        print(f"{row[0]}, {row['house']}")
