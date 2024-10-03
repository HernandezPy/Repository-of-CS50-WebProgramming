import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few commnand-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)

        if 'name' not in reader.fieldnames or 'house' not in reader.fieldnames:
            sys.exit("Not a CSV file")

        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                last_name, first_name = row['name'].split(', ')
                writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

except FileNotFoundError:
    sys.argv(f'Could not read {input_file}')

