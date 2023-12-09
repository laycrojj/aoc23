""" Solution for Round 3 of AOC """

import pathlib
import os.path

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

def get_numbers_in_line(line: str) -> list:
    """ Return a List of Tuples containing the start index 
    and length of the number on the line """
        
    line_numbers: list = []

    number_end = 0

    for index, character in enumerate(line):
        if index >= number_end and character in NUMBERS:
            start = index
            length = get_number_length(line[index + 1::])
            line_numbers.append((start,length))
            number_end = index + length

    return line_numbers

def check_kernel(position: tuple,list_2d: list, kernel: list) -> bool:
    """ Check if condition is True for any kernel index in the 2d list """

    for i in range(position[1]):
        for indexes in kernel:
            y = 1 + indexes[0]
            x = position[0] + i + indexes[1]
            try:
                if "." != list_2d[y][x] and list_2d[y][x] not in NUMBERS:
                    return True
            except(IndexError):
                print(x, "out of range!")

    return False

def get_adjacent_hits(prev_line :list,this_line: list,next_line: list,number_list: list) -> list:
    """ Return Numbers in the line with adjacent Symbols """

    valid_numbers = []
    line_array = [prev_line,this_line,next_line]

    for i in number_list:
        if check_kernel(i,line_array,KERNEL):
            valid_numbers.append(i)

    return valid_numbers

def get_line_numbers(valid_numbers: list, line: str) -> int:
    """ add up all the numbers in a line """

    total = 0

    for number in valid_numbers:
        number_end_index = number[0] + number[1]
        total += int(line[number[0]:number_end_index])

    return total

def get_line_score(line: str, prev_line: str, next_line: str) -> int:
    """ Calculate the score from the given line """

    # Get Numbers in line
    number_list = get_numbers_in_line(line)

    # Check for hits symbol hits
    valid_numbers_list = get_adjacent_hits(prev_line,line,next_line,number_list)

    # print(valid_numbers_list)

    # Get Number from hit
    return get_line_numbers(valid_numbers_list, line)

def main():
    """ Main Entry Point """

    current_directory = pathlib.Path(__file__).parent.resolve()
    input_file = os.path.join(current_directory,"input.txt")

    with open(input_file, "r", encoding="utf-8") as calibration_doc:
        content = [line.rstrip() for line in calibration_doc]

    running_total = 0

    for index, line in enumerate(content):
        prev_index = index - 1 if index -1 >= 0 else 0
        next_index = index + 1 if index +1 < len(content) else index
        running_total += get_line_score(line,content[prev_index],content[next_index])
        print(running_total)

    print(running_total)

if __name__ == "__main__":

    main()
