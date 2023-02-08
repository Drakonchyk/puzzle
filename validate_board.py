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
    pass

def validate_color(board: list) -> bool:
    """
    check nums in colors on board
    returns bool
    >>> validate_color("**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****")
    True
    """
    row_board = [list(i) for i in board]
    column_board = [[row_board[i][j] for i in range(len(row_board))]
                     for j in range(len(row_board[0]))]
    check_new_rows = ["".join(row_board[index]) + "".join(column_board[-(index+1)])
                      for index in range(len(row_board[0]))]

    return validate_row(check_new_rows)

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
