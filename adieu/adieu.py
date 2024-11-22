import inflect

def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        pass


p = inflect.engine()
names_list = p.join(names)
print(f"Adieu, adieu, to {names_list}")


main()
