import csv, sys, os

if len(sys.orgv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.orgv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(")
