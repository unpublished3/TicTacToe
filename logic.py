import random
import copy
import customtkinter as tk

def turn(board):
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell  == "X":
                x_count += 1
            elif cell  == "O":
                o_count += 1
    return "X" if x_count == o_count else "O"


def terminal(board):
    return check_win(board, "X") or check_win(board, "O") or check_draw(board)


def check_win(board, piece):
    return (
        check_diagonal(board, piece)
        or check_horizontal(board, piece)
        or check_vertical(board, piece)
    )


def check_horizontal(board, piece):
    for i in range(3):
        if all(board[i][j]  == piece for j in range(3)):
            return True
    return False


def check_vertical(board, piece):
    for i in range(3):
        if all(board[j][i]  == piece for j in range(3)):
            return True
    return False


def check_diagonal(board, piece):
    if all(board[i][i]  == piece for i in range(3)):
        return True
    if all(board[i][2 - i]  == piece for i in range(3)):
        return True
    return False


def check_draw(board):
    for row in board:
        for cell in row:
            if cell  not in ["X", "O"]:
                return False

    return True


def utility(board):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    return 0


def actions(board):
    print(board)
    board_actions = []

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell  == "":
                board_actions.append((i, j))
    return board_actions


def result(board, action):
    board_copy = copy.deepcopy(board)

    current_turn = turn(board)
    board_copy[action[0]][action[1]] = current_turn
    return board_copy

def minimax(board):
    board_actions = actions(board)
    action = random.choice(board_actions)

    return action
