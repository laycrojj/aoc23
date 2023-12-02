import pathlib
import os.path

digits = {

    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    'one': '1',
    'two': '2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
}

def get_line_digits(line: str):
    """ Get the first digit in the supplied string """

    line_length = len(line)

    first_position = line_length
    last_position = 0

    first_value = None
    last_value = None

    found_first = False
    found_last = False

    # check every digit against string one by one
    for digit, value in digits.items():

        if not found_first:
            first_digit_match = line.find(digit,0,first_position)

            if first_digit_match == 0:
                first_value = value
                found_first = True
            elif -1 < first_digit_match < first_position:
                first_position = first_digit_match + len(digit)
                first_value = value


        if not found_last:
            last_digit_match = line.rfind(digit,last_position)
            if last_digit_match != -1 and last_digit_match + len(digit) == line_length:
                last_value = value
                found_last = True
            elif last_digit_match >= last_position:
                last_position = last_digit_match
                last_value = value

    return first_value + last_value


def main():
    """ Main Entry Point """

    current_directory = pathlib.Path(__file__).parent.resolve()
    input_file = os.path.join(current_directory,"input.txt")

    with open(input_file, "r", encoding="utf-8") as calibration_doc:
        content = [line for line in calibration_doc]

    running_total = 0

    for line in content:

        line_number = int(get_line_digits(line.rstrip()))

        running_total += line_number

    print(running_total)

if __name__ == "__main__":

    main()
