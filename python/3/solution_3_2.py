""" Solution for Round 3 pt2 of AOC """

import pathlib
import os.path
from collections import defaultdict

NUMBERS: list = [ str(x) for x in range(10) ]
KERNEL: list = [
            (-1,-1),
            (-1,0),
            (-1,1),
            (0,-1),
            (0,1),
            (1,-1),
            (1,0),
            (1,1),
          ]

def get_number_length(line_portion: list) -> int:
    """ Get the Length of the current number in the line """

    number_length = 1

    for character in line_portion:
        if character in NUMBERS:
            number_length += 1
        else:
            return number_length

    return number_length

def get_numbers_in_line(line: str, line_index: int) -> list:
    """ Return a List of Tuples containing the start index 
    and length of the number on the line """
        
    line_numbers: list = []

    number_end = 0

    for index, character in enumerate(line):
        if index >= number_end and character in NUMBERS:
            start = index
            length = get_number_length(line[index + 1::])
            line_numbers.append((start,length,line_index))
            number_end = index + length

    return line_numbers

def check_kernel(position: tuple,list_2d: list, kernel: list,centre_index: int):
    """ Check if condition is True for any kernel index in the 2d list """

    for i in range(position[1]):
        for indexes in kernel:
            y = 1 + indexes[0]
            x = position[0] + i + indexes[1]
            try:
                if list_2d[y][x] == "*":
                    return (centre_index + indexes[0],x)
            except(IndexError):
                print(x, "out of range!")

    return False

def get_adjacent_hits(line_list: list, line_index: int, number_list: list, valid_numbers: defaultdict):
    """ Return Numbers in the line with adjacent Symbols """

    prev_index = line_index - 1 if line_index -1 >= 0 else 0
    next_index = line_index + 1 if line_index +1 < len(line_list) else line_index
    line_array = [line_list[prev_index],line_list[line_index],line_list[next_index]]

    for i in number_list:
        adjacent_asterix = check_kernel(i,line_array,KERNEL,line_index)
        if adjacent_asterix is not False:
            valid_numbers[adjacent_asterix].append(i)


def get_line_numbers(valid_numbers: list, line: str) -> int:
    """ add up all the numbers in a line """

    total = 0

    for number in valid_numbers:
        number_end_index = number[0] + number[1]
        total += int(line[number[0]:number_end_index])

    return total

def calculate_asterix_score(asterix_hits: list, content: list) -> int:
    """ Return the score from the given asterisk """

    if len(asterix_hits) != 2:
        return 0

    n1 = asterix_hits[0]
    n2 = asterix_hits[1]

    n1_end = n1[0]+n1[1]
    n2_end = n2[0]+n2[1]

    return int(content[n1[2]][n1[0]:n1_end]) * int(content[n2[2]][n2[0]:n2_end])


def main():
    """ Main Entry Point """

    current_directory = pathlib.Path(__file__).parent.resolve()
    input_file = os.path.join(current_directory,"input.txt")

    with open(input_file, "r", encoding="utf-8") as calibration_doc:
        content = [line.rstrip() for line in calibration_doc]

    valid_numbers_dict = defaultdict(list)
    running_total = 0

    for index, line in enumerate(content):
        # Get Numbers in line
        number_list = get_numbers_in_line(line,index)

        # Check for hits symbol hits
        get_adjacent_hits(content,index,number_list,valid_numbers_dict)

    # Get Number from hit
    for key in valid_numbers_dict:
        running_total += calculate_asterix_score(valid_numbers_dict[key],content)

    print(running_total)

if __name__ == "__main__":

    main()
