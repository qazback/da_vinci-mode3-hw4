import sys
import os
import csv
from tabulate import tabulate

def format_pizza_table(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [row for row in reader]

    return tabulate(data, headers, tablefmt="grid")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    csv_file = sys.argv[1]
    if not csv_file.endswith('.csv'):
        sys.exit("Not a CSV file")

    if not os.path.exists(csv_file):
        sys.exit("File does not exist")

    try:
        table = format_pizza_table(csv_file)
        print(table)
    except FileNotFoundError:
        sys.exit("The specified file does not exist.")
