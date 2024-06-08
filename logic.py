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
