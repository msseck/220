"""
Name:Marietou Seck
lab10.py

Problem: This program demonstrates constructs used throughout the semester to build a game of tic-tac-toe.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def board_list():
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return list_b


def draw_board(board):
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("---------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("---------")
    print("{} | {} | {} ".format(board[6], board[7], board[8]))
    print("---------")


def x_or_o(board, position, mark):
    if mark == 'x' or mark == 'o':
        board[eval(position) - 1] = mark
    else:
        print("use x or o")


def valid(board, position):
    if str(board[eval(position)-1]).isnumeric():
        return True
    else:
        return False


def game_won(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    else:
        return False


def game_over(board):
    if game_won(board):
        return True
    for i in board:
        if str(i).isnumeric():
            return False
    return True


def main():
    print("Instructions: Player 1 and Player two will pick from either x or o to mark their spot.\n"
          "The first player to get three in a row with their respective mark wins and the game is over.\n "
          "If all spots are marked without a win, the game is over and y ")

    board = board_list()
    while not(game_over(board)):
        draw_board(board)
        position = input("Which spot?:")
        character = input("x or o:")
        if valid(board, position):
            x_or_o(board, position, character)
    if game_won(board):
        print(character, "is the winner!")

    else:
        print("Game Over")
    pass


main()
