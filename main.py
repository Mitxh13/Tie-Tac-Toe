import random as rd
import botplayer
from botplayer import system_move

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for col in row:
            print("|", col, end="    ", sep="  ")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board, dict_moves, used_moves):
    move_value = int(input("Enter your move number: "))
    if move_value in used_moves:
        print("Invalid move! Already used by someone!.")
        return
    used_moves.append(move_value)
    dict_moves[move_value] = "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == move_value:
                board[i][j] = "X"

    display_board(board)
    if victory_for(dict_moves):
        return True
    sys_move = system_move(used_moves, dict_moves)
    dict_moves[sys_move] = "O"
    for i in range(3):
        for j in range(3):
            if board[i][j] == sys_move:
                board[i][j] = "O"
    display_board(board)
    if victory_for(dict_moves):
        return True

    return False 



def victory_for(dict_moves):
    winning_moves = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),   
        (1, 4, 7), (2, 5, 8), (3, 6, 9),    
        (1, 5, 9), (3, 5, 7)               
    ]
    for combo in winning_moves:
        if all(dict_moves.get(pos) == "O" for pos in combo):
            print("Bot wins!")

            return True
        elif all(dict_moves.get(pos) == "X" for pos in combo):
            print("You win!")
            return True
    if len(dict_moves) == 9:
        print("It's a draw!")
        return True
    return False


def main():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    dict_moves = {}
    used_moves = []

    display_board(board)

    while True:
        if enter_move(board, dict_moves, used_moves): 
            break


#--------------------------main-----------------------------------
#calling main funtion to start game
main()
