from pyfiglet import Figlet
import sys
import random
import argparse

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    parser = argparse.ArgumentParser(description="Generate text in a FIGlet font.")
    parser.add_argument("-f", "--font", help="specify the font to use", type=str, required=False)
    args = parser.parse_args()


    if args.font:
        if args.font not in available_fonts:
            sys.exit(f"Error: '{args.font}' is not a valid font.")
        font = args.font
    else:
        font = random.choice(available_fonts)

    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    if len(sys.argv) not in [1, 3]:
        sys.exit("")

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Usege: figlet.py or figlet.py -f FONT")

    main()
