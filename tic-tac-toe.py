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
