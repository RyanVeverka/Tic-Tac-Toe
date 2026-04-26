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

def get_move(board, player):
    '''
    Purpose: Get a VALID move from user
    Input: board (list of lists), player (str)
    Output: (row, col)
    '''
    while True:
        try:
            user_input = input(f"Player {player}, enter row and column (e.g., 1 2): ").strip()
            parts = user_input.split()
            # Check correct format
            if len(parts) != 2:
                print("Error: Enter exactly TWO numbers separated by a space.")
                continue
            row, col = int(parts[0]), int(parts[1])
            # Check bounds
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Error: Row and column must be between 0 and 2.")
                continue
            # Check if cell is empty
            if board[row][col] != ' ':
                print("Error: That cell is already taken.")
                continue
            return row, col
        except ValueError:
            print("Error: Please enter valid integers (e.g., 0 1).")

def switch_player(current_player):
    '''
    Purpose: Alternate between players
    Input: current_player (str)
    Output: next player (str)
    '''
    return 'O' if current_player == 'X' else 'X'

def initialize_board():
    '''
    Purpose: Create an empty 3x3 board
    Input: None
    Output: board (list of lists)
    '''
    return [[' ' for _ in range(3)] for _ in range(3)]

def play_game():
    '''
    Purpose: Main game controller
    Input: None
    Output: None
    '''
    board = initialize_board()
    current_player = 'X'
    while True:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break
        # Check for draw
        if is_draw(board):
            print_board(board)
            print("\nThe game is a draw!")
            break
        # Switch turns
        current_player = switch_player(current_player)


# ============================================
# Program Entry Point
# ============================================
if __name__ == "__main__":
    play_game()