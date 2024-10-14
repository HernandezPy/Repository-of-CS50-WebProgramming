import sys, os
from PIL import Image


if len(sys.orgv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.orgv) > 3:
    sys.exit("Too many command-line arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

valid_extensions = [".jpg", ".jpeg", ".png"]
input_ext = os.path.splitext(input_path)[1].lower()
output_ext = os.path.splitext(output_path)[2].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid output")

def main():
    shirt = Image.open("input_file") as img:
        img.save("after")



