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

    colours = ["RED","GREEN","BLUE"]

    for colour in colours:
        if colour in colour_input.upper():
            return colour
        
def update_largest_amounts(single_round: str, current_largest: dict) -> dict:
    """ Return an updated RGB dict of largest amounts given a rounds input """

    cube_pulls : list[str] = single_round.split(",")

    for cube_pull in cube_pulls:
        colour = get_colour(cube_pull)
        amount = get_amount(cube_pull)
        if current_largest[colour] < amount:
            current_largest[colour] = amount
        
    return current_largest

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
    largest_amounts : dict = {
        "RED": 0,
        "GREEN": 0,
        "BLUE": 0,
    }

    for single_round in rounds:
        largest_amounts = update_largest_amounts(single_round, largest_amounts)

    power : int = largest_amounts["RED"] * largest_amounts["GREEN"] * largest_amounts["BLUE"]

    return power

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
