import random

print("Welcome to Text based Tic-Tac-Toe game!!!")
# user_choice = input("Do you want 'O' or 'X'? Type to start the game.")

row_1 = ["_", "_", "_"]
row_2 = ["_", "_", "_"]
row_3 = ["_", "_", "_"]

all_rows = [row_1, row_2, row_3]

def print_game_changes():
    for row in all_rows:
        print(' | '.join(row))


def check_win_condition():
    for row in all_rows:
        if row.count(row[0]) == len(row) and row[0]!= "_":
            print(f"We have a Winner. \nWinner is {row[0]}")
            return

    for a in range(0, 2):
        if all_rows[0][a] == all_rows[1][a] == all_rows[2][a] and all_rows[2][a] != "_":
            print(f"We have a Winner. \nWinner is {all_rows[0][a]}")
            return

    if all_rows[0][0] == all_rows[1][1] == all_rows[2][2] and all_rows[2][2] != "_":
        print(f"We have a Winner. \nWinner is {all_rows[0][0]}")
        return

    elif all_rows[0][2] == all_rows[1][1] == all_rows[2][0] and all_rows[2][0] != "_":
        print(f"We have a Winner. \nWinner is {all_rows[0][2]}")
        return


