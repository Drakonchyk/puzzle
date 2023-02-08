"""
Puzzle Game
"""

def validate_row(board):
    """
    check rows on board
    returns bool
    """
    pass

def validate_column(board):
    """
    check columns on board
    returns bool
    """
    new_board = []
    i = 0
    while len(new_board) < len(board[0]):
        elem_board = ''
        for j in board:
            elem_board += j[i]
        i += 1
        new_board.append(elem_board)
    return validate_row(new_board)

def validate_color(board):
    """
    check nums in colors on board
    returns bool
    """
    pass

def validate_board(board):
    """
    Main function to check if board is valid
    """
    if validate_row(board) and validate_color(board) and validate_column(board):
        return True
    return False

board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]

print(validate_board(board))