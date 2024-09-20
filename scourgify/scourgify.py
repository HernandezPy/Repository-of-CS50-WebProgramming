with open("before.csv",) as file:
    for line in file:
        row = line.rstrip().split(",")
        print({row[0]}, {row[1]},)
