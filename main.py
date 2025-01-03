import random

print("Welcome to Text based Tic-Tac-Toe game!!!")
user_choice = input("Do you want 'O' or 'X'? Type to start the game.")

while user_choice not in ["X" , "O"]:
    print("Invalid input. Please put valid input.")
    user_choice = input("Do you want 'O' or 'X'? Type to start the game.")

if user_choice == "X":
    computer_choice_symbol = "O"
else:
    computer_choice_symbol = "X"

row_1 = ["_", "_", "_"]
row_2 = ["_", "_", "_"]
row_3 = ["_", "_", "_"]

all_rows = [row_1, row_2, row_3]

def print_game_changes():
    line = 0
    for row in all_rows:
        print(' | '.join(row))
        if line <2:
            print("_________")
            line += 1


def check_win_condition():
    print("\n")
    for row in all_rows:
        if row.count(row[0]) == len(row) and row[0]!= "_":
            print(f"We have a Winner. \nWinner is {row[0]}")
            return True

    for a in range(0, 2):
        if all_rows[0][a] == all_rows[1][a] == all_rows[2][a] and all_rows[2][a] != "_":
            print(f"We have a Winner. \nWinner is {all_rows[0][a]}")
            return True


    if all_rows[0][0] == all_rows[1][1] == all_rows[2][2] and all_rows[2][2] != "_":
        print(f"We have a Winner. \nWinner is {all_rows[0][0]}")
        return True


    elif all_rows[0][2] == all_rows[1][1] == all_rows[2][0] and all_rows[2][0] != "_":
        print(f"We have a Winner. \nWinner is {all_rows[0][2]}")
        return True


def computer_choice():
    not_done = True
    while not_done:
        chosen_row = random.choice(all_rows)
        chosen_index = all_rows.index(chosen_row)
        chosen_column = random.choice(chosen_row)
        chosen_2nd_index = chosen_row.index(chosen_column)
        if chosen_column == "_":
            all_rows[chosen_index][chosen_2nd_index] = computer_choice_symbol
            not_done = False

game_not_finished = True
print_game_changes()
while game_not_finished:
    input_row = int(input("\nWhich row would you like to put symbol in?"))
    input_column = int(input("Which column would you like to put symbol in?"))

    if all_rows[input_row -1][input_column -1] == "_":
        all_rows[input_row - 1][input_column - 1] = user_choice
        computer_choice()
        print_game_changes()
    if check_win_condition():
        print("Game finished")
        game_not_finished = False
