import sys
import readline
import inflect

def main():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    farewell_message = generate_farewell(names)
    print(farewell_message)


def generate_farewell(names):
    p = inflect.engine()
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    else:
        names_list = p.join(names)
        return f"Adieu, adieu, to {names_list}"

if __name__ == "__main__":
    main()
