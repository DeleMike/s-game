# 6.009 Lab 2: Snekoban

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}

game_just_started = True


def get_player_pos(arr):
    """
    Given a description of a game state, this returns the position of of the '[player]' object.
    If it returns (-1,-1) then that means object wasn't found,
    """
    row_pos = 0
    col_pos = 0
    z_pos = 0
    n_col_pos = 0

    # trying to access the "['player']" object and get its location.
    for rows in arr:
        for cols in rows:
            for z_row in cols:
                if z_row == 'player':
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
    # print('player position is: ', '(', row, ',', col, ')')

    # determine what pos to move
    dx, dy = direction_vector[direction]
    # print('dx, dy = (', dx, ',', dy, ')')

    new_row = row + dx
    new_col = col + dy

    # down movement check; if the proposed down movement
    # has exceeded the box boundaries then keep it stagnant
    if new_row == max_col_len:
        new_row = max_col_len - 1

    # up movement check; if the proposed up movement
    # has exceeded the box boundaries then keep it stagnant
    if new_row < 0:
        new_row = 0

    # left movement; if the proposed left movement
    # has exceeded the box boundaries then keep it stagnant
    if new_col < 0:
        new_col = 0

    # right movement; if the proposed right movement
    # has exceeded the box boundaries then keep it stagnant
    if new_col == max_row_len:
        new_col = max_row_len - 1

    # print('player position is now: ', '(', new_row, ',', new_col, ')')

    # swap position
    # before we swap we have to check if the position we want to move to is not a wall
    # If it is a wall, then the 'Player' Object must remain where it is.

    # check if player and target are in the same position
    # if arr[row][col] == ['target', 'player']:
    #     print('a target and a player on the same spot.')
    #     # check if there is a target in front of the computer. If there is, place it on top of the target
    #     if direction == 'right':
    #         if not arr[new_row][new_col]:
    #             arr[row][col] = ['target']
    #             arr[new_row][new_col] = ['player']
    #         elif arr[new_row][new_col] == ['wall']:
    #             pass
    #         elif arr[new_row][new_col + 1] == ['wall']:
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target']:
    #             if arr[new_row][new_col + 1] == ['target']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 # arr[new_row][new_col + 1] = ['target']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row][new_col + 1] == ['computer']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col + 1] = ['computer']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col + 1] = []
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['computer']:
    #             if arr[new_row][new_col + 1] == ['target']:
    #                 arr[new_row][new_col + 1] = ['target', 'computer']
    #                 arr[new_row][new_col] = ['player']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['player']
    #                 arr[new_row][new_col + 1] = ['computer']
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target', 'computer']:
    #             if not arr[new_row][new_col + 1]:
    #                 arr[new_row][new_col + 1] = ['computer']
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row][new_col + 1] == ['computer']:
    #                 pass
    #             elif arr[new_row][new_col + 1] == ['target', 'computer']:
    #                 pass
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col + 1] = ['target', 'computer']
    #                 arr[row][col] = ['target']
    #         elif not arr[new_row][new_col + 1]:
    #             arr[new_row][new_col + 1] = ['computer']
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col + 1] == ['target']:
    #             print('reached a target')
    #             if arr[row][col] == ['target', 'player']:
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[row][col] = []
    #             arr[new_row][new_col] = ['player']
    #             arr[new_row][new_col + 1] = ['target', 'computer']
    #
    #     elif direction == 'left':
    #         if not arr[new_row][new_col]:
    #             arr[row][col] = ['target']
    #             arr[new_row][new_col] = ['player']
    #         elif arr[new_row][new_col] == ['wall']:
    #             pass
    #         elif arr[new_row][new_col - 1] == ['wall']:
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target']:
    #             if arr[new_row][new_col - 1] == ['target']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 # arr[new_row][new_col - 1] = ['target']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row][new_col - 1] == ['computer']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col - 1] = ['computer']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col - 1] = []
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['computer']:
    #             if arr[new_row][new_col - 1] == ['target']:
    #                 arr[new_row][new_col - 1] = ['target', 'computer']
    #                 arr[new_row][new_col] = ['player']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['player']
    #                 arr[new_row][new_col - 1] = ['computer']
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target', 'computer']:
    #             if not arr[new_row][new_col - 1]:
    #                 arr[new_row][new_col - 1] = ['computer']
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row][new_col - 1] == ['computer']:
    #                 pass
    #             elif arr[new_row][new_col - 1] == ['target', 'computer']:
    #                 pass
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row][new_col - 1] = ['target', 'computer']
    #                 arr[row][col] = ['target']
    #         elif not arr[new_row][new_col - 1]:
    #             arr[new_row][new_col - 1] = ['computer']
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col - 1] == ['target']:
    #             print('reached a target')
    #             if arr[row][col] == ['target', 'player']:
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[row][col] = []
    #             arr[new_row][new_col] = ['player']
    #             arr[new_row][new_col - 1] = ['target', 'computer']
    #
    #     elif direction == 'up':
    #         if not arr[new_row][new_col]:
    #             arr[row][col] = ['target']
    #             arr[new_row][new_col] = ['player']
    #         elif arr[new_row][new_col] == ['wall']:
    #             pass
    #         elif arr[new_row - 1][new_col] == ['wall']:
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target']:
    #             if arr[new_row - 1][new_col] == ['target']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 # arr[new_row - 1][new_col] = ['target']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row - 1][new_col] == ['computer']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row - 1][new_col] = ['computer']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row - 1][new_col] = []
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['computer']:
    #             if arr[new_row - 1][new_col] == ['target']:
    #                 arr[new_row - 1][new_col] = ['target', 'computer']
    #                 arr[new_row][new_col] = ['player']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['player']
    #                 arr[new_row - 1][new_col] = ['computer']
    #                 arr[row][col] = ['target']
    #         elif arr[new_row - 1][new_col] == ['target', 'computer']:
    #             if not arr[new_row][new_col]:
    #                 arr[new_row - 1][new_col] = ['computer']
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row - 1][new_col] == ['computer']:
    #                 pass
    #             elif arr[new_row - 1][new_col] == ['target', 'computer']:
    #                 pass
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row - 1][new_col] = ['target', 'computer']
    #                 arr[row][col] = ['target']
    #         elif not arr[new_row - 1][new_col]:
    #             arr[new_row - 1][new_col] = ['computer']
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row - 1][new_col] == ['target']:
    #             if arr[row][col] == ['target', 'player']:
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[row][col] = []
    #             arr[new_row][new_col] = ['player']
    #             arr[new_row - 1][new_col] = ['target', 'computer']
    #
    #     elif direction == 'down':
    #         if not arr[new_row][new_col]:
    #             arr[row][col] = ['target']
    #             arr[new_row][new_col] = ['player']
    #         elif arr[new_row][new_col] == ['wall']:
    #             pass
    #         elif arr[new_row + 1][new_col] == ['wall']:
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['target']:
    #             if arr[new_row + 1][new_col] == ['target']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 # arr[new_row + 1][new_col] = ['target']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row + 1][new_col] == ['computer']:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row + 1][new_col] = ['computer']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row + 1][new_col] = []
    #                 arr[row][col] = ['target']
    #         elif arr[new_row][new_col] == ['computer']:
    #             if arr[new_row + 1][new_col] == ['target']:
    #                 arr[new_row + 1][new_col] = ['target', 'computer']
    #                 arr[new_row][new_col] = ['player']
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[new_row][new_col] = ['player']
    #                 arr[new_row + 1][new_col] = ['computer']
    #                 arr[row][col] = ['target']
    #         elif arr[new_row + 1][new_col] == ['target', 'computer']:
    #             if not arr[new_row][new_col]:
    #                 arr[new_row + 1][new_col] = ['computer']
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[row][col] = ['target']
    #             elif arr[new_row + 1][new_col] == ['computer']:
    #                 pass
    #             elif arr[new_row + 1][new_col] == ['target', 'computer']:
    #                 pass
    #             else:
    #                 arr[new_row][new_col] = ['target', 'player']
    #                 arr[new_row + 1][new_col] = ['target', 'computer']
    #                 arr[row][col] = ['target']
    #         elif not arr[new_row + 1][new_col]:
    #             arr[new_row + 1][new_col] = ['computer']
    #             arr[new_row][new_col] = ['target', 'player']
    #             arr[row][col] = ['target']
    #
    #         elif arr[new_row + 1][new_col] == ['target']:
    #             print('reached a target')
    #             if arr[row][col] == ['target', 'player']:
    #                 arr[row][col] = ['target']
    #             else:
    #                 arr[row][col] = []
    #             arr[new_row][new_col] = ['player']
    #             arr[new_row + 1][new_col] = ['target', 'computer']
    #     return arr

    if arr[new_row][new_col] == ['wall']:
        pass
    elif arr[row][col] == ['target', 'player']:
        if not arr[new_row][new_col]:
            arr[row][col] = ['target']
            arr[new_row][new_col] = ['player']
        elif direction == 'right':
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            elif arr[new_row][new_col - 1] == ['wall']:
                pass
            elif not arr[new_row][new_col + 1]:
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                else:
                    arr[new_row][new_col + 1] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            elif arr[new_row][new_col] == ['computer']:
                if arr[new_row][new_col + 1] == ['wall']:
                    pass
                elif arr[new_row + 1][new_col] == ['computer']:
                    pass
                else:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player', 'player']
                    arr[new_row][new_col + 1] = ['target', 'computer']
        elif direction == 'left':
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            elif arr[new_row][new_col - 1] == ['wall']:
                pass
            elif not arr[new_row][new_col - 1]:
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                else:
                    arr[new_row][new_col - 1] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            elif arr[new_row][new_col] == ['computer']:
                if arr[new_row][new_col - 1] == ['wall']:
                    pass
                elif arr[new_row + 1][new_col] == ['computer']:
                    pass
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row][new_col - 1] = ['target', 'computer']
                    arr[row][col] = ['target']
        elif direction == 'up':
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            elif arr[new_row][new_col - 1] == ['wall']:
                pass
            elif not arr[new_row - 1][new_col]:
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                else:
                    arr[new_row - 1][new_col] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            elif arr[new_row][new_col] == ['computer']:
                if arr[new_row - 1][new_col] == ['wall']:
                    pass
                elif arr[new_row + 1][new_col] == ['computer']:
                    pass
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row - 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']
        elif direction == 'down':
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            elif arr[new_row + 1][new_col] == ['wall']:
                pass
            elif not arr[new_row + 1][new_col]:
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                else:
                    arr[new_row + 1][new_col] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            elif arr[new_row][new_col] == ['computer']:
                if arr[new_row + 1][new_col] == ['wall']:
                    pass
                elif arr[new_row + 1][new_col] == ['computer']:
                    pass
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row + 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']

    elif arr[new_row][new_col] == ['computer']:
        if direction == 'right':
            if arr[new_row][new_col + 1] == ['target']:
                arr[new_row][new_col + 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']

            elif not arr[new_row][new_col + 1]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row][new_col + 1]
                arr[new_row][new_col + 1] = temp
        elif direction == 'left':
            if arr[new_row][new_col - 1] == ['target']:
                arr[new_row][new_col - 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']

            elif not arr[new_row][new_col - 1]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row][new_col - 1]
                arr[new_row][new_col - 1] = temp
        elif direction == 'up':
            if arr[new_row - 1][new_col] == ['target']:
                arr[new_row - 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']

            elif not arr[new_row - 1][new_col]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row - 1][new_col]
                arr[new_row - 1][new_col] = temp
        elif direction == 'down':
            if arr[new_row + 1][new_col] == ['target']:
                arr[new_row + 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']

            elif not arr[new_row + 1][new_col]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row + 1][new_col]
                arr[new_row + 1][new_col] = temp
    elif arr[new_row][new_col] == ['target']:
        arr[row][col] = []
        arr[new_row][new_col] = ['target', 'player']
    elif arr[new_row][new_col] == ['target', 'computer']:
        if direction == 'right':
            if arr[new_row][new_col + 1] == ['target']:
                arr[new_row][new_col + 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col + 1]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row][new_col + 1] = ['computer']

        elif direction == 'left':
            if arr[new_row][new_col - 1] == ['target']:
                arr[new_row][new_col - 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row][new_col - 1]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row][new_col - 1] = ['computer']

        elif direction == 'up':
            if arr[new_row - 1][new_col] == ['target']:
                arr[new_row - 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row - 1][new_col]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row - 1][new_col] = ['computer']

        elif direction == 'down':
            if arr[new_row + 1][new_col] == ['target']:
                arr[new_row + 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            elif not arr[new_row + 1][new_col]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row + 1][new_col] = ['computer']

    else:
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

    # check if any single ['computer'] and ['target'] still exists
    # check if number of computers == targets

    # first, we get the total number of computers and targets and compare

    computer_count = 0
    target_count = 0
    comp_and_target_found = 0
    for rows in game:
        for obj in rows:
            if obj == ['computer']:
                computer_count += 1
            elif obj == ['target']:
                target_count += 1
            elif obj == ['target', 'computer']:
                comp_and_target_found += 1

    # print('The number of computers are: ', computer_count, '\nThe number of targets are: ', target_count)

    if computer_count == 0 and target_count == 0 and comp_and_target_found > 0:
        return True

    return False


def step_game(game, direction):
    """
    Given a game representation (of the form returned from new_game), return a
    new game representation (of that same form), representing the updated game
    after running one step of the game.  The user's input is given by
    direction, which is one of the following: {'up', 'down', 'left', 'right'}.

    This function should not mutate its input.
    """
    global game_just_started
    game_just_started = False
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

    # check if all the computers and targets are successfully placed correctly
    player_has_won = victory_check(game)

    # if the game just started and all the computers and targets are not successfully placed correctly then display the
    # game board
    if game_just_started and not player_has_won:
        return game
    # if the game just started and all the computers and targets are already successfully placed correctly then
    # display the game board
    elif game_just_started and player_has_won:
        return game

    # else, just display the game board
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
