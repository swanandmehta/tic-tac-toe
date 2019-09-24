# Tic Tac Toe Game


def start_game():
    config = setup()

    is_win = False

    draw_board(config)

    while is_win is not True:
        user = get_user(config)
        update_user_input(user, config)
        draw_board(config)
        is_win = validate_win(config, user)
        if is_win is not True:
            switch_user(config)

    winner = get_winner(config)

    congratulate_winner(winner)


def congratulate_winner(winner):
    print(str(winner)+" won the game \nThank you for playing")


def get_winner(config):
    return config.get("active_user").get("name")


def switch_user(config):
    if config.get("active_user") == config.get("player").get("player1"):
        active_user = {"active_user": config.get("player").get("player2")}
        config.update(active_user)
    elif config.get("active_user") == config.get("player").get("player2"):
        active_user = {"active_user": config.get("player").get("player1")}
        config.update(active_user)
    else:
        config["active_user"] = config.get("player").get("player1")


def validate_win(config, user):
    is_win = check_column(config, user)

    if is_win is not True:
        is_win = check_rows(config, user)

    if is_win is not True:
        is_win = check_diagonal(config, user)

    return is_win


def check_diagonal(config, user):

    pointer = 1
    value_to_add = 0
    element_counter = 0

    elements_in_diagonal = []

    while element_counter < config.get("board").get("size"):
        elements_in_diagonal.append(pointer + value_to_add)
        value_to_add = value_to_add + 1
        pointer = pointer + config.get("board").get("size")
        element_counter = element_counter + 1

    if is_completed(elements_in_diagonal, user, config) is True:
        return True

    pointer = config.get("board").get("size")
    value_to_remove = 0
    element_counter = 0
    elements_in_diagonal = []

    while element_counter < config.get("board").get("size"):
        elements_in_diagonal.append(pointer - value_to_remove)
        pointer = pointer + config.get("board").get("size")
        value_to_remove = value_to_remove + 1
        element_counter = element_counter + 1

    if is_completed(elements_in_diagonal, user, config) is True:
        return True

    return False


def check_rows(config, user):
    row_counter = 0
    row_pointer = 1

    while row_counter < config.get("board").get("size"):

        elements_in_row = []
        row_element_counter = 0

        while row_element_counter < config.get("board").get("size"):
            elements_in_row.append(row_pointer)
            row_pointer = row_pointer + 1
            row_element_counter = row_element_counter + 1

        if is_completed(elements_in_row, user, config) is True:
            return True

        row_counter = row_counter + 1

    return False


def check_column(config, user):
    col_counter = 1

    while col_counter <= config.get("board").get("size"):

        col_element_counter = 0
        col_pointer = col_counter
        col_element_pos_list = []

        while col_element_counter < config.get("board").get("size"):
            if col_pointer <= config.get("board").get("size"):
                col_element_pos_list.append(col_pointer)
                col_pointer = col_pointer + config.get("board").get("size")
                pass
            else:
                col_element_pos_list.append(col_pointer)
                col_pointer = col_pointer + config.get("board").get("size")

            col_element_counter = col_element_counter + 1

        if is_completed(col_element_pos_list, user, config) is True:
            return True

        col_counter = col_counter + 1

    return False


def is_completed(col_element_pos_list, user, config):
    key = user.get("key")
    moves = config.get("moves")

    for pos in col_element_pos_list:
        move = moves.get(pos)
        if move is None or move != key:
            return False

    return True


def update_user_input(user, config):
    message = user.get("name")+" please select your move \n"
    user_input = int(input(message))

    config.get("moves")[user_input] = user.get("key")

    return user_input


def get_user(config):

    if config.get("active_user") is None:
        config["active_user"] = config.get("player").get("player1")

    return config.get("active_user")


def draw_board(config):
    board = ""
    row_counter = 0
    element_count = 1
    moves = config.get("moves")

    while row_counter < config.get("board").get("size"):
        col_counter = 0
        board = board + "|"
        while col_counter < config.get("board").get("size"):
            board = board + "_"+str(element_count)+"_|"
            element_count = element_count + 1
            col_counter = col_counter + 1

        board = board + "\n"
        row_counter = row_counter + 1

        for item in moves.items():
            board = board.replace(str(item[0]), item[1])

    print(board)


def setup():

    config = {
        "board": {
            "size": 3
        },
        "player": {
            "player1": {
                "name": "Player 1",
                "key": "X"
            },
            "player2": {
                "name": "Player 2",
                "key": "O"
            }
        },
        "moves": {},
        "active_user": None
    }

    return config


start_game()
