with open("before.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name}, {house}")
