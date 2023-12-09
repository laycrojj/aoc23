""" Solution for Round 2 of AOC """

import pathlib
import os.path

CUBE_AMOUNTS = {

    "RED": 12,
    "GREEN": 13,
    "BLUE": 14,

}

def get_amount(amount_input: str) -> int:
    """ Read the amount from the input """

    return int(amount_input.split()[0])

def get_colour(colour_input: str) -> str:
    """ Read the colour from the input """

    COLOURS = ["RED","GREEN","BLUE"]

    for colour in COLOURS:
        if colour in colour_input.upper():
            return colour

def round_possible(single_round: str) -> bool:
    """ Returns a boolean depending on whether the game is possible """

    cube_pulls : list[str] = single_round.split(",")

    for cube_pull in cube_pulls:
        colour = get_colour(cube_pull)
        amount = get_amount(cube_pull)
        if CUBE_AMOUNTS[colour] < amount:
            return False

    return True

def get_game_id(line_input: str) -> int:
    """ Returns the id associated with the game input """

    game_id: int = int(line_input.split(":")[0].split()[1])

    return game_id

def get_rounds(line_input: str) -> list[str]:
    """ Get a list of rounds in a game as a list"""

    full_input = line_input.split(":")[1]
    rounds_input = list( full_input.split(";") )

    return rounds_input

def calculate_game_score(line_input: str) -> int:
    """ Calculates if the game is possible and returns the appropriate score """

    game_id : int = get_game_id(line_input)
    rounds : list[str] = get_rounds(line_input)

    for single_round in rounds:
        if round_possible(single_round) is False:
            return 0

    return game_id

def main():
    """ Main Entry Point """

    current_directory = pathlib.Path(__file__).parent.resolve()
    input_file = os.path.join(current_directory,"input.txt")

    with open(input_file, "r", encoding="utf-8") as calibration_doc:
        content = [line.rstrip() for line in calibration_doc]

    running_total = 0

    for line in content:

        game_score: int = calculate_game_score(line)
        running_total += game_score
        print("Game Score:", game_score)

    print(running_total)

if __name__ == "__main__":

    main()
