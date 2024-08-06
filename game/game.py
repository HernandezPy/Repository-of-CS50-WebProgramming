import random

def get_positive_integer(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass


def main():
    while True:
        level = get_positive_integer("Level: ")
        if level > 0:
            break

    number_to_guess = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < number_to_guess:
            print("Too small!")
        elif guess > number_to_guess:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()


