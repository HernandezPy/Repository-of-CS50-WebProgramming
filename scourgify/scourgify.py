with open("before.csv", "r") as file:
    reader = file.reader(file)
    for row in reader:
        print(row)
