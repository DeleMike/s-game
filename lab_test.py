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
  [[], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"], ["wall"]],
  [[], ["wall"], [], [], [], [], [], ["wall"]],
  [[], ["wall"], [], ["target"], ["computer"], ["target"], [], ["wall"]],
  [
    ["wall"],
    ["wall"],
    [],
    ["computer"],
    ["player"],
    ["computer"],
    [],
    ["wall"]
  ],
  [["wall"], [], [], ["target"], ["computer"], ["target"], [], ["wall"]],
  [["wall"], [], [], [], [], [], [], ["wall"]],
  [
    ["wall"],
    ["wall"],
    ["wall"],
    ["wall"],
    ["wall"],
    ["wall"],
    ["wall"],
    ["wall"]
  ]
]


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

    print('max_row_len: ', max_row_len)
    print('max_col_len: ', max_col_len)
    # get ["player"] position
    row, col = get_player_pos(arr)
    print('player position is: ', '(', row, ',', col, ')')

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
    temp = arr[row][col]
    arr[row][col] = arr[new_row][new_col]
    arr[new_row][new_col] = temp

    return arr


# get arr_row length and arr_col length
# max_y_len = 0
# max_x_len = 0
# for rows in game:
#     max_y_len = len(rows)
#     for cols in rows:
#         continue
#     max_x_len += 1
#
# print('Row length is: ', max_y_len)
# print('Col length is: ', max_x_len)

# print('Player position in the game is: ', get_player_pos(game))
# print('I want to move the player "right": ', move_player(game, 'right'))
num = 0
while num < 10:
    move_player(game, 'down')
    # print('I want to move the player "right": ', move_player(game, 'right'))
    num += 1
