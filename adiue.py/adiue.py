import sys
import readline # for handling the Control-D
import inflect

def main():
    print("Enter names (Ctrl-D to end):")

    # Reading names until Ctrl-D (EOF) is encountered
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Generate the farewell message
    farewell_message = generate_farewell(name)
    print(farewell_message)


def generate_farewell(names):
    p = inflect.engine()
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    else:
        # Use inflect to create the list with proper grammar
        names_list = p.join(names)
        return f"Adieu, adieu, to {names_list}"

if __name__ == "__main__":
    main()
