from tabulate import tabulate


def main():
    data = {

        "a": ("Full Mouth Restoration", 250),
        "b": ("Dental Implants", 50),
        "c": ("Teeth Whitening", 100),
        "d": ("General Dentistry", 150),
        "e": ("Crown and Bridgework", 75),
    }

    table_of_information(data)
    total_cost = job_cost(data)
    if total_cost > 0:
        discount_in_advance(total_cost)


def table_of_information(data):
    table = [[key.upper(), work, f"${cost}"] for key, (work, cost) in data.items()]
    headers = ["Option", "Service", "Cost"]
    print(tabulate(table, headers, tablefmt="grid"))


def job_cost(data):
    selection = input("Select the service that you want: (a, b, c, d, e): ").lower().strip()
    if selection in data:
        work, cost = data[selection]
        print(f"You selected: {work}. you will pay ${cost:.2f} ")
        return cost
    else:
        print("Please select a valid option")
        return 0


def discount_in_advance(total):
    print("Did you know that if you pay in advance you receive a 50% discount?")
    advance = input("Would you like to pay in advance? [yes/no]: ").strip().lower()
    discount_total = total * 0.5
    if advance == "yes":
        print(f"Your amount to pay with discount is: ${discount_total:.2f}")
    elif advance == "no":
        print(f"You have to pay full amount: ${total:.2f}")
    else:
        print("Invalid option")
        print("You have to choose yes or no")


if __name__ == "__main__":
    main()
