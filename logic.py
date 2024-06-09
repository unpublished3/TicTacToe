import copy


def turn(board):
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell.get() == "X":
                x_count += 1
            elif cell.get() == "O":
                o_count += 1
    return "X" if x_count == o_count else "O"


def terminal(board):
    if check_win(board, "X") or check_win(board, "O") or check_draw(board):
        return True
    return False


def check_win(board, piece):
    if (
        check_diagonal(board, piece)
        or check_horizontal(board, piece)
        or check_vertical(board, piece)
    ):
        return True

    return False


def check_horizontal(board, piece):
    for i in range(3):
        if (
            board[i][0].get() == piece
            and board[i][1].get() == piece
            and board[i][2].get() == piece
        ):
            return True
    return False


def check_vertical(board, piece):
    for i in range(3):
        if (
            board[0][i].get() == piece
            and board[1][i].get() == piece
            and board[1][i].get() == piece
        ):
            return True
    return False


def check_diagonal(board, piece):
    if (
        board[0][0].get() == piece
        and board[1][1].get() == piece
        and board[2][2].get() == piece
    ):
        return True

    if (
        board[0][2].get() == piece
        and board[1][1].get() == piece
        and board[2][0].get() == piece
    ):
        return True

    return False


def check_draw(board):
    count = 0
    for row in board:
        for cell in row:
            if cell.get() == "X" or cell.get() == "O":
                count += 1

    if count == 9:
        return True
    return False


def utility(board):
    if check_draw(board):
        return 0
    if check_win(board, "X"):
        return 1
    return -1


def actions(board):
    board_actions = []

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell.get() == "":
                board_actions.append((i, j))
    return board_actions


def result(board, action):
    board_copy = copy.deepcopy(board)
    current_turn = turn(board)
    board_copy[action[0]][action[1]].set(current_turn)
    return board_copy
