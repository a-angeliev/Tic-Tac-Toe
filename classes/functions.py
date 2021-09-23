from classes.classes import Game


def create_class():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player_one = input("Player one name: ")
    player_two = input("Player two name: ")

    while True:
        sign_one = input(f"{player_one} would you like to play with 'X' or 'O'")
        if sign_one == 'O' or sign_one == 'X':
            sing_two = "X" if sign_one == "O" else "O"
            break
        else:
            print("Incorrect input. Please choose correct symbol!")
    turn = 1

    return Game(board, player_one, player_two, sign_one, sing_two, turn)


def start_info(game_info):
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    if game_info.turn_info() == 1:
        print(f"{game_info.player_one_info()} start first")
    else:
        print("error")


def is_free_position(game_info, chosen_position):
    if 0 < chosen_position < 10:
        row = (chosen_position - 1) // 3
        col = (chosen_position - 1) % 3
        if game_info.board_info()[row][col] == " ":
            return True
        else:
            print("This position has already been selected")
            return False
    else:
        print("Chose correct number!")


def is_not_winer(game_info):
    lists = game_info.board_info()
    for row in range(3):
        if lists[row].count("X") == 3 or lists[row].count("O") == 3:
            if lists[row][0] == "X":
                if game_info.sign_one_info() == "X":
                    print(f"{game_info.player_one_info()} is the winner.")
                    exit(0)
                else:
                    print(f"{game_info.player_two_info()} is the winner.")
                    exit(0)
            else:
                if game_info.sign_one_info() == "O":
                    print(f"{game_info.player_one_info()} is the winner.")
                    exit(0)
                else:
                    print(f"{game_info.player_two_info()} is the winner.")
                    exit(0)
    zipped_rows = zip(*lists)
    transpose_matrix = [list(row) for row in zipped_rows]
    for row in range(3):
        if transpose_matrix[row].count("X") == 3 or transpose_matrix[row].count("O") == 3:
            if transpose_matrix[row][0] == "X":
                if game_info.sign_one_info() == "X":
                    print(f"{game_info.player_one_info()} is the winner.")
                    exit(0)
                else:
                    print(f"{game_info.player_two_info()} is the winner.")
                    exit(0)
            else:
                if game_info.sign_one_info() == "O":
                    print(f"{game_info.player_one_info()} is the winner.")
                    exit(0)
                else:
                    print(f"{game_info.player_two_info()} is the winner.")
                    exit(0)
    winning_el = None
    if lists[0][0] == "X" and lists[1][1] == "X" and lists[2][2] == "X":
        winning_el = "X"
    elif lists[0][0] == "O" and lists[1][1] == "O" and lists[2][2] == "O":
        winning_el = "O"
    elif lists[0][2] == "X" and lists[1][1] == "X" and lists[2][0] == "X":
        winning_el = "X"
    elif lists[0][2] == "O" and lists[1][1] == "O" and lists[2][0] == "O":
        winning_el = "O"

    if winning_el == game_info.sign_one_info():
        print(f"{game_info.player_one_info()} is the winner.")
        exit(0)
    if winning_el == game_info.sign_two_info():
        print(f"{game_info.player_two_info()} is the winner.")
        exit(0)
    return True


def is_no_free_space(game_info):
    for row in range(3):
        if " " in game_info.board_info()[row]:
            return False
    return True
