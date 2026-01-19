board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(player):
    combos = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for combo in combos:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def is_full():
    return " " not in board

def play_game():
    current_player = "X"
    while True:
        print_board()
        move = input(f"Player {current_player}, choose position (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue
        move = int(move) - 1
        if board[move] != " ":
            print("Spot already taken. Try again.")
            continue
        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f" Player {current_player} wins!")
            break
        if is_full():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
