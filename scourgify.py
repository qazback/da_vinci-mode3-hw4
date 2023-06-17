import sys
import csv

def clean_data(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = ['first', 'last', 'house']

            with open(output_file, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    name_parts = row['name'].split(', ')
                    first_name = name_parts[1]
                    last_name = name_parts[0]

                    writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})

        print(f"Data cleaned successfully. The results are stored in {output_file}")
    except FileNotFoundError:
        sys.exit("The specified input file does not exist.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit("Please provide exactly two command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_data(input_file, output_file)
