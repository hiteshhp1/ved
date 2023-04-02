def print_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")

def check_win(board, player):
    win_combos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        move = int(input(f"{current_player}'s turn. Enter a position (1-9): "))
        if board[move-1] != " ":
            print("That position is already taken. Try again.")
            continue
        board[move-1] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()
