with open("before.csv",) as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]}, {row[1]}")
