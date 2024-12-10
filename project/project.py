def main():
    data = {

        "a": ("Full Mouth Restoration", 250),
        "b": ("Dental Implants", 50),
        "c": ("Teeth Whitening", 100),
        "d": ("General Dentistry", 150),
        "e": ("Crown and Bridgework", 75),
    }

    table_of_information(data)
    discount_in_advance(data)


def table_of_information(data):
    print("Customer Services Available")
    for key, (work, cost) in data.items():
        print(f"{key}: {work} - ${cost}")


def job_cost(data):
    customer = input("Select the job to be done: (a, b, c, d, e): ")
    if customer in data:
        work, total = data[customer]
        print(f"You selected: {work}, you're paying ${total}")
        return total
    else:
        print("Please select a valid option")
        return 0


def discount_in_advance(data):
    total = job_cost(data)
    if total == 0:
        return
    print("Did you know that if you pay in advance you receive a 50% discount?")
    advance = input("Would you like to pay in advance? [yes/no]: ").strip().lower()
    if advance == "yes":
        print(f"Your amount to pay with discount is: ${total * 0.5:.2f}")
    else:
        print(f"You have to pay full amount: ${total:.2f}")


if __name__ == "__main__":
    main()
