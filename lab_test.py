# game = [
#     [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]],
#     [["wall"], [], [], [], [], ["wall"]],
#     [["wall"], [], ["wall"], ["player"], [], ["wall"]],
#     [["wall"], [], ["computer"], ["target", "computer"], [], ["wall"]],
#     [["wall"], [], ["target"], ["target", "computer"], [], ["wall"]],
#     [["wall"], [], [], [], [], ["wall"]],
#     [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]]
# ]

game = [
    [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]],
    [["wall"], [], [], [], [], ["wall"]],
    [["wall"], [], ["wall"], ["player"], [], ["wall"]],
    [["wall"], [], ["target", "computer"], ["target", "computer"], [], ["wall"]],
    [["wall"], [], [], ["target", "computer"], [], ["wall"]],
    [["wall"], [], [], [], [], ["wall"]],
    [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]]
]

# game = [
#   [[], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]],
#   [[], ["wall"], [], [], [], [], [], ["wall"]],
#   [[], ["wall"], [], ["target"], ["computer"], ["target"], [], ["wall"]],
#   [
#     ["wall"],
#     ["wall"],
#     [],
#     ["computer"],
#     ["player"],
#     ["computer"],
#     [],
#     ["wall"]
#   ],
#   [["wall"], [], [], ["target"], ["computer"], ["target"], [], ["wall"]],
#   [["wall"], [], [], [], [], [], [], ["wall"]],
#   [
#     ["wall"],
#     ["wall"],
#     ["wall"],
#     ["wall"],
#     ["wall"],
#     ["wall"],
#     ["wall"],
#     ["wall"]
#   ]
# ]


# game = [
#   [[], [], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]],
#   [[], [], ["wall"], [], ["target"], ["target"], ["player"], ["wall"]],
#   [[], [], ["wall"], [], ["computer"], ["computer"], [], ["wall"]],
#   [[], [], ["wall"], ["wall"], [], ["wall"], ["wall"], ["wall"]],
#   [[], [], [], ["wall"], [], ["wall"], [], []],
#   [[], [], [], ["wall"], [], ["wall"], [], []],
#   [["wall"], ["wall"], ["wall"], ["wall"], [], ["wall"], [], []],
#   [["wall"], [], [], [], [], ["wall"], ["wall"], []],
#   [["wall"], [], ["wall"], [], [], [], ["wall"], []],
#   [["wall"], [], [], [], ["wall"], [], ["wall"], []],
#   [["wall"], ["wall"], ["wall"], [], [], [], ["wall"], []],
#   [[], [], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], []]
# ]

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

    # print('max_row_len: ', max_row_len)
    # print('max_col_len: ', max_col_len)
    # get ["player"] position
    row, col = get_player_pos(arr)
    # print('player position is: ', '(', row, ',', col, ')')

    # determine what pos to move
    dx, dy = direction_vector[direction]
    # print('dx, dy = (', dx, ',', dy, ')')

    new_row = row + dx
    new_col = col + dy

    # down movement check
    if new_row == max_col_len:
        new_row = max_col_len - 1

    # up movement check
    if new_row < 0:
        new_row = 0

    # left movement
    if new_col < 0:
        new_col = 0

    # right movement
    if new_col == max_row_len:
        new_col = max_row_len - 1

    # print('player position is now: ', '(', new_row, ',', new_col, ')')

    # swap position
    # before we swap we have to check if the position we want to move to is not a wall
    # If it is a wall, then the 'Player' Object must remain where it is.

    temp = arr[row][col]
    if arr[new_row][new_col] == ['wall']:
        print('reached a wall')
    elif arr[new_row][new_col] == ['computer']:
        if direction == 'right' and arr[new_row][new_col + 1] == []:
            print('there is a space')
    else:
        arr[row][col] = arr[new_row][new_col]
        arr[new_row][new_col] = temp

    return arr


# num = 0
# while num < 5:
#     move_player(game, 'right')
#     # print('I want to move the player "right": ', move_player(game, 'right'))
#     num += 1


def check_victory_condition(arr):
    # check if any single ['computer'] and ['target'] still exists
    # check if number of computers == targets

    # first, we get the total number of computers and targets and compare

    computer_count = 0
    target_count = 0
    for rows in arr:
        for obj in rows:
            if obj == ['computer']:
                computer_count += 1
            elif obj == ['target']:
                target_count += 1

    print('The number of computers are: ', computer_count, '\nThe number of targets are: ', target_count)

    if computer_count == 0 and target_count == 0:
        return True

    return False


# print('The function returned: ', check_victory_condition(game))


def check_arr():
    ls = [[[], [], [], ["wall"], ["wall"], ["wall"], ["wall"]], [[], [], [], ["wall"], [], [], ["wall"]],
          [[], [], [], ["wall"], ["player"], [], ["wall"]],
          [["wall"], ["wall"], ["wall"], ["wall"], [], ["target", "computer"], ["wall"]],
          [["wall"], [], [], [], [], ["target", "computer"], ["wall"]],
          [["wall"], [], ["wall"], [], [], ["target", "computer"], ["wall"]],
          [["wall"], [], [], [], [], ["wall"], ["wall"]],
          [["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], []]]

    for i in ls:
        for j in i:
            print(i)


# check_arr()
