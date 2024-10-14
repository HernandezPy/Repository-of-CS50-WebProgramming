import sys, os
from PIL import Image


def main():
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

    if input_ext != output_ext:
        sys.exit("Input and Output have different extensions")

    if not os.path.isfile(input_path):
        sys.exit("Input does not exist")


    try:
        input_img = Image.open(input_path)
        shirt_img = Image.open("shirt.png")

        resized_img = ImageOps.fit(input_img, size)
        resized_img.paste(shirt_img, shirt_img)
        resized_img.save(output_path)

    except FileNotFoundError:
        sys.exit("File not found")
    except Exception as e:
        sys.exit(f"Error: {e})

if __name__ == "__main__":
    main()





