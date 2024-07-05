def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Tacos": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    while True:
         try:
            item = input('Item: ').strip().title()
            if item in menu:
                total_cost += menu[item]
                print(f"${total_cost:.2f}")
         except EOFError:
           print("\n")
           break

if __name__ == "__main__":
    main()

