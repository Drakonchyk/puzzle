"""
Puzzle Game
"""

def validate_row(board):
    """
    check rows on board
    returns bool
    >>> validate_row(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 3  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    >>> validate_row(["**** ****",\
 "***1 ****",\
 "**  2****",\
 "* 4 1****",\
 "     9 6 ",\
 " 5  84  *",\
 "3   2  **",\
 "  7  2***",\
 "  2  ****"])
    True
    """
    for i in board:
        for j in i:
            if j.isdigit() and i.count(j) > 1:
                return False
    return True

def validate_column(board):
    """
    check columns on board
    returns bool
    """
    pass

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