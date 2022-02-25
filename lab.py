# 6.009 Lab 2: Snekoban

import json
import typing

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}


def get_player_pos(arr):
    """
    Given a description of a game state, this returns the position of of the '[player]' object.
    If it returns (-1,-1) then that means object wasn't found,
    """
    row_pos = 0
    col_pos = 0
    z_pos = 0
    n_col_pos = 0

    for rows in arr:
        for cols in rows:
            for z_row in cols:
                if z_row == 'player':
                    # print('Found \'player\' Pos: ', (row_pos, z_pos))
                    # print('Array containing "player": ', rows)
                    # get pos of "3" in rows arr
                    for row in rows:
                        for col in row:
                            if col == 'player':
                                return row_pos, n_col_pos
                        n_col_pos += 1
                    break
                z_pos += 1
            col_pos += 1
        row_pos += 1

    return -1, -1


def move_player(arr, direction):
    """
    Move player position based on given direction.
    """
    # first get the MAXIMUM LENGTH FOR ROWS AND COLUMNS
    max_row_len = 0
    max_col_len = 0
    for rows in arr:
        max_row_len = len(rows)
        for _ in rows:
            continue
        max_col_len += 1

    # get ["player"] position
    row, col = get_player_pos(arr)

    # determine what pos to move
    dx, dy = direction_vector[direction]
    new_row = row + dx
    new_col = col + dy

    # perform checks to prevent IndexOutBoundError
    if new_row == max_row_len - 1:
        # print('Row value has reached its max threshold')
        new_row = row

    if new_col == max_col_len - 1:
        # print('Col value has reached its max threshold')
        new_col = col

    # if the proposed row position to shift to is less than Zero then remain stagnant
    if new_row < 0:
        new_row = 0
        # print('Row value has reached its min threshold')

    # if the proposed column position to shift to is less than Zero then remain stagnant
    if new_col < 0:
        new_col = 0
        # print('Col value has reached its min threshold')

    # swap position

    temp = arr[row][col]
    arr[row][col] = arr[new_row][new_col]
    arr[new_row][new_col] = temp

    return arr


def new_game(level_description):
    """
    Given a description of a game state, create and return a game
    representation of your choice.

    The given description is a list of lists of lists of strs, representing the
    locations of the objects on the board (as described in the lab writeup).

    For example, a valid level_description is:

    [
        [[], ['wall'], ['computer']],
        [['target', 'player'], ['computer'], ['target']],
    ]

    The exact choice of representation is up to you; but note that what you
    return will be used as input to the other functions.
    """
    return level_description


def victory_check(game):
    """
    Given a game representation (of the form returned from new_game), return
    a Boolean: True if the given game satisfies the victory condition, and
    False otherwise.
    """
    pass


def step_game(game, direction):
    """
    Given a game representation (of the form returned from new_game), return a
    new game representation (of that same form), representing the updated game
    after running one step of the game.  The user's input is given by
    direction, which is one of the following: {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    return move_player(game, direction)


def dump_game(game):
    """
    Given a game representation (of the form returned from new_game), convert
    it back into a level description that would be a suitable input to new_game
    (a list of lists of lists of strings).

    This function is used by the GUI and the tests to see what your game
    implementation has done, and it can also serve as a rudimentary way to
    print out the current state of your game for testing and debugging on your
    own.
    """
    return game


def solve_puzzle(game):
    """
    Given a game representation (of the form returned from new game), find a
    solution.

    Return a list of strings representing the shortest sequence of moves ("up",
    "down", "left", and "right") needed to reach the victory condition.

    If the given level cannot be solved, return None.
    """
    pass


if __name__ == "__main__":
    pass
