# ============================================
# Tic-Tac-Toe (2 Player - Terminal Based)
# ============================================


def print_board(board):
    '''
    Purpose: Display the current board
    Input: board (list of lists)
    Output: None
    '''
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    '''
    Purpose: Check if a player has won
    Input: board (list of lists), player (str)
    Output: True/False
    '''

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    '''
    Purpose: Determine if the game is a draw
    Input: board (list of lists)
    Output: True/False
    '''
    for row in board:
        if ' ' in row:
            return False
    return True