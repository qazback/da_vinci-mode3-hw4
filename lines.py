import sys
import os


def count_lines_of_code(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    code_lines = 0
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            code_lines += 1

    return code_lines


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.exists(filename):
        sys.exit("File does not exist")

    try:
        num_lines = count_lines_of_code(filename)
        print(f"Number of lines of code: {num_lines}")
    except FileNotFoundError:
        sys.exit("The specified file does not exist.")
