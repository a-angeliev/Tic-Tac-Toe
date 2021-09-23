from classes.functions import *

game = create_class()
start_info(game)
while True:
    # Validate chosen position input
    while True:
        if game.turn_info() == 1:
            chosen_position = int(input(f"{game.player_one_info()} choose a free position [1 - 9]: "))
        else:
            chosen_position = int(input(f"{game.player_two_info()} choose a free position [1 - 9]: "))

        if is_free_position(game, chosen_position):
            print(is_free_position(game, chosen_position))
            break
    # Make a movement
    game.move(chosen_position)
    # Display current board info
    game.display_board()
    # Check if there is a winner
    is_not_winer(game)
    # Check if there are no free spaces
    if is_no_free_space(game):
        print("There is not winner!")
        exit(0)
