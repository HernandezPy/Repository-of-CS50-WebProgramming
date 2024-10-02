with open("before.csv") as file:
    for row in file:
        print(f"{row[0]}, {row[2]}")
