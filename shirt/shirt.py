import sys, os
from PIL import Image


if len(sys.orgv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.orgv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

def main():
    with Image.open("input_file") as img:
        img.save("after")



