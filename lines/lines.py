import sys
import os


def count_lines_of_code(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        loc = 0

        for line in lines:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("#"):
                loc += 1

        return loc
    except FileNotFoundError:
        sys.exit(f"File '{filename}' not found.")


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    if not os.path.isfile(filename):
        sys.exit(f"File not found.")

    loc = count_lines_of_code(filename)
    print(loc)


if __name__ == "__main__":
    main()
