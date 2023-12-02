import pathlib
import os.path

digits = [ str(x) for x in range(10) ]

def get_first_digit(line: str):
    """ Get the first digit in the supplied string """

    for character in line:
        if character in digits:
            return character

    return None

def get_last_digit(line: str):
    """ Get the first digit in the supplied string """

    return get_first_digit(line[::-1])


def main():
    """ Main Entry Point """

    current_directory = pathlib.Path(__file__).parent.resolve()
    input_file = os.path.join(current_directory,"input.txt")

    with open(input_file, "r", encoding="utf-8") as calibration_doc:
        content = [line for line in calibration_doc]

    running_total = 0

    for line in content:

        first = get_first_digit(line)
        last = get_last_digit(line)
        line_number = int(first + last)

        running_total += line_number

    print(running_total)

if __name__ == "__main__":

    main()