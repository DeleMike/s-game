# 6.009 Lab 2: Snekoban

# NO ADDITIONAL IMPORTS!


direction_vector = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}

# to check if the game just started
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

    # if a wall is in front of the player should remain still
    if arr[new_row][new_col] == ['wall']:
        pass
    # this code block checks applies if there is a ['target', 'player'] object besides the player object
    elif arr[row][col] == ['target', 'player']:
        # if ['target', 'player'] and ['player'] wants to move to [] (the empty space) in front of it
        if not arr[new_row][new_col]:
            arr[row][col] = ['target']
            arr[new_row][new_col] = ['player']
        # if direction is eastwards
        elif direction == 'right':
            # player wants to move to another target
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            # player wants to move to an empty space
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            # player wants to a position where a wall is occupying
            elif arr[new_row][new_col + 1] == ['wall']:
                pass
            elif not arr[new_row][new_col + 1]:
                # player wants to move eastward and the column after the desired destination is empty then move it
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                # player wants to move eastward but the column after the desired destination has a
                # ['target', 'computer'] so we have to adjust it as per stated rules
                elif arr[new_row][new_col] == ['target', 'computer']:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row][new_col + 1] = ['computer']
                    arr[row][col] = ['target']
                # fallback action but code block is poised for deletion.
                else:
                    arr[new_row][new_col + 1] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            # player wants to move eastward and the desired destination has a ['computer']
            elif arr[new_row][new_col] == ['computer']:
                # to the right of the computer is a ['wall']. Do not move.
                if arr[new_row][new_col + 1] == ['wall']:
                    pass
                # to the right of the computer is another computer or maybe another ['target', 'computer']. Don't move
                elif arr[new_row][new_col + 1] == ['computer'] or arr[new_row][new_col + 1] == ['target', 'computer']:
                    pass
                # else move object as desired.
                else:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player', 'player']
                    arr[new_row][new_col + 1] = ['target', 'computer']
            # player wants to move eastward and the desired destination has a ['target', 'computer']
            elif arr[new_row][new_col] == ['target', 'computer']:
                # if the object to the right of ['target', 'computer'] is a [computer] or [target , computer],
                # DO NOT MOVE
                if arr[new_row][new_col + 1] == ['computer'] or arr[new_row][new_col + 1] == ['target', 'computer']:
                    pass
                # else, carry out desired movements
                else:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row][new_col + 1] = ['target', 'computer']
                    arr[row][col] = ['target']
        # if direction is westwards
        elif direction == 'left':
            # player wants to move to another target
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            # player wants to move to an empty space
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            # player wants to a position where a wall is occupying
            elif arr[new_row][new_col - 1] == ['wall']:
                pass
            elif not arr[new_row][new_col - 1]:
                # player wants to move westward and the column before the desired destination is empty then move it
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                # player wants to move westward but the column before the desired destination has a
                # ['target', 'computer'] so we have to adjust it as per stated rules
                elif arr[new_row][new_col] == ['target', 'computer']:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row][new_col - 1] = ['computer']
                    arr[row][col] = ['target']
                # fallback action but code block is poised for deletion.
                else:
                    arr[new_row][new_col - 1] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            # player wants to move westward and the desired destination has a ['computer']
            elif arr[new_row][new_col] == ['computer']:
                # to the left of the computer is a ['wall']. Do not move.
                if arr[new_row][new_col - 1] == ['wall']:
                    pass
                # to the left of the computer is another computer or maybe another ['target', 'computer']. Don't move
                elif arr[new_row][new_col - 1] == ['computer'] or arr[new_row][new_col - 1] == ['target', 'computer']:
                    pass
                # else move object as desired.
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row][new_col - 1] = ['target', 'computer']
                    arr[row][col] = ['target']
            # player wants to move westward and the desired destination has a ['target', 'computer']
            elif arr[new_row][new_col] == ['target', 'computer']:
                # if the object to the left of ['target', 'computer'] is a [computer] or [target , computer],
                # DO NOT MOVE
                if arr[new_row][new_col - 1] == ['computer'] or arr[new_row][new_col - 1] == ['target', 'computer']:
                    pass
                # else, carry out desired movements
                else:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row][new_col - 1] = ['target', 'computer']
                    arr[row][col] = ['target']
        # if direction is northwards
        elif direction == 'up':
            # player wants to move to another target
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            # player wants to move to an empty space
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            # player wants to a position where a wall is occupying
            elif arr[new_row - 1][new_col] == ['wall']:
                pass
            elif not arr[new_row - 1][new_col]:
                # player wants to move northwards and the column before the desired destination is empty then move it
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                # player wants to move northward but the column before the desired destination has a
                # ['target', 'computer'] so we have to adjust it as per stated rules
                elif arr[new_row][new_col] == ['target', 'computer']:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row - 1][new_col] = ['computer']
                    arr[row][col] = ['target']
                # fallback action but code block is poised for deletion.
                else:
                    arr[new_row - 1][new_col] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            # player wants to move westward and the desired destination has a ['computer']
            elif arr[new_row][new_col] == ['computer']:
                # in front of the computer is a ['wall']. Do not move.
                if arr[new_row - 1][new_col] == ['wall']:
                    pass
                # in front of the computer is another computer or maybe another ['target', 'computer']. Don't move
                elif arr[new_row - 1][new_col] == ['computer'] or arr[new_row - 1][new_col] == ['target', 'computer']:
                    pass
                # else move object as desired.
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row - 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']
            # player wants to move northward and the desired destination has a ['target', 'computer']
            elif arr[new_row][new_col] == ['target', 'computer']:
                # if the object is in front of ['target', 'computer'] is a [computer] or [target , computer],
                # DO NOT MOVE
                if arr[new_row - 1][new_col] == ['computer'] or arr[new_row - 1][new_col] == ['target', 'computer']:
                    pass
                # else, carry out desired movements
                else:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row - 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']
        # if direction is southwards
        elif direction == 'down':
            # player wants to move to another target
            if arr[new_row][new_col] == ['target']:
                arr[row][col] = ['target']
                arr[new_row][new_col] = ['target', 'player']
            # player wants to move to an empty space
            elif not arr[new_row][new_col]:
                arr[new_row][new_col] = ['player']
                arr[row][col] = ['target']
            # player wants to a position where a wall is occupying
            elif arr[new_row + 1][new_col] == ['wall']:
                pass
            elif not arr[new_row + 1][new_col]:
                # player wants to move southwards and the column before the desired destination is empty then move it
                if not arr[new_row][new_col]:
                    arr[row][col] = ['target']
                    arr[new_row][new_col] = ['player']
                # player wants to move southward but the column before the desired destination has a
                # ['target', 'computer'] so we have to adjust it as per stated rules
                elif arr[new_row][new_col] == ['target', 'computer']:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row + 1][new_col] = ['computer']
                    arr[row][col] = ['target']
                # fallback action but code block is poised for deletion.
                else:
                    arr[new_row + 1][new_col] = ['computer']
                    arr[new_row][new_col] = ['player']
                    arr[row][col] = ['target']
            # player wants to move southward and the desired destination has a ['computer']
            elif arr[new_row][new_col] == ['computer']:
                # in front of the computer is a ['wall']. Do not move.
                if arr[new_row + 1][new_col] == ['wall']:
                    pass
                # in front of the computer is another computer or maybe another ['target', 'computer']. Don't move
                elif arr[new_row + 1][new_col] == ['computer'] or arr[new_row + 1][new_col] == ['target', 'computer']:
                    pass
                # else move object as desired.
                else:
                    arr[new_row][new_col] = ['player']
                    arr[new_row + 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']
            # player wants to move southward and the desired destination has a ['target', 'computer']
            elif arr[new_row][new_col] == ['target', 'computer']:
                # if the object is in front of ['target', 'computer'] is a [computer] or [target , computer],
                # DO NOT MOVE
                if arr[new_row + 1][new_col] == ['computer'] or arr[new_row + 1][new_col] == ['target', 'computer']:
                    pass
                # else, carry out desired movements
                else:
                    arr[new_row][new_col] = ['target', 'player']
                    arr[new_row + 1][new_col] = ['target', 'computer']
                    arr[row][col] = ['target']
    # this code checks if desired location is a ['computer']
    elif arr[new_row][new_col] == ['computer']:
        # if direction is right,
        if direction == 'right':
            # and the object to the right of the computer is a ['target'] then move the computer on top of the target
            # and adjust others appropriately as per stated rules
            if arr[new_row][new_col + 1] == ['target']:
                arr[new_row][new_col + 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']
            # else, perform three variable swapping
            elif not arr[new_row][new_col + 1]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row][new_col + 1]
                arr[new_row][new_col + 1] = temp
        # if direction is left,
        elif direction == 'left':
            # and the object to the left of the computer is a ['target'] then move the computer on top of the target
            # and adjust others appropriately as per stated rules
            if arr[new_row][new_col - 1] == ['target']:
                arr[new_row][new_col - 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']
            # else, perform three variable swapping
            elif not arr[new_row][new_col - 1]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row][new_col - 1]
                arr[new_row][new_col - 1] = temp
        # if direction is up,
        elif direction == 'up':
            # and the object in front of the computer is a ['target'] then move the computer on top of the target
            # and adjust others appropriately as per stated rules
            if arr[new_row - 1][new_col] == ['target']:
                arr[new_row - 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']
            # else, perform three variable swapping
            elif not arr[new_row - 1][new_col]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row - 1][new_col]
                arr[new_row - 1][new_col] = temp
        # if direction is down,
        elif direction == 'down':
            # and the object behind the computer is a ['target'] then move the computer on top of the target
            # and adjust others appropriately as per stated rules
            if arr[new_row + 1][new_col] == ['target']:
                arr[new_row + 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['player']
            # else, perform three variable swapping
            elif not arr[new_row + 1][new_col]:
                temp = arr[new_row][new_col]
                arr[new_row][new_col] = arr[row][col]
                arr[row][col] = arr[new_row + 1][new_col]
                arr[new_row + 1][new_col] = temp
    # if the desired location has a target, then place the player on top of it
    elif arr[new_row][new_col] == ['target']:
        arr[row][col] = []
        arr[new_row][new_col] = ['target', 'player']
    # if the desired location has a ['target', 'computer'] object
    elif arr[new_row][new_col] == ['target', 'computer']:
        # if direction is right,
        if direction == 'right':
            # if to the right of the ['target', 'computer'] is a ['target'] then move the computer to the next target
            if arr[new_row][new_col + 1] == ['target']:
                arr[new_row][new_col + 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            # else, if it is empty then move as per rules
            elif not arr[new_row][new_col + 1]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row][new_col + 1] = ['computer']
        # if direction is left,
        elif direction == 'left':
            # if to the left of the ['target', 'computer'] is a ['target'] then move the computer to the next target
            if arr[new_row][new_col - 1] == ['target']:
                arr[new_row][new_col - 1] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            # else, if it is empty then move as per rules
            elif not arr[new_row][new_col - 1]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row][new_col - 1] = ['computer']
        # if direction is up,
        elif direction == 'up':
            # if the front of the ['target', 'computer'] is a ['target'] then move the computer to the next target
            if arr[new_row - 1][new_col] == ['target']:
                arr[new_row - 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            # else, if it is empty then move as per rules
            elif not arr[new_row - 1][new_col]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row - 1][new_col] = ['computer']
        # if direction is down,
        elif direction == 'down':
            # if behind of the ['target', 'computer'] is a ['target'] then move the computer to the next target
            if arr[new_row + 1][new_col] == ['target']:
                arr[new_row + 1][new_col] = ['target', 'computer']
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
            # else, if it is empty then move as per rules
            elif not arr[new_row + 1][new_col]:
                arr[row][col] = []
                arr[new_row][new_col] = ['target', 'player']
                arr[new_row + 1][new_col] = ['computer']
    # here, we perform basic movement of player by simple swapping
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
    # if the player press any of the direction keys then we should note that the game has already started a game ago.
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
