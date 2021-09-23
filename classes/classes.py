class Game:
    def __init__(self, board, player_one, player_two, sign_one, sign_two, turn):
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.sign_one = sign_one
        self.sign_two = sign_two
        self.turn = turn

    def board_info(self):
        return list(self.board)

    def turn_info(self):
        return self.turn

    def player_one_info(self):
        return self.player_one

    def player_two_info(self):
        return self.player_two

    def sign_one_info(self):
        return self.sign_one

    def sign_two_info(self):
        return self.sign_two

    def show_all(self):
        print(f"Player one is {self.player_one} and play with '{self.sign_one}'")
        print(f"Player two is {self.player_two} and play with '{self.sign_two}'")
        if self.turn == 1:
            print(f"Its {self.player_one} turn")
        else:
            print(f"Its {self.player_two} turn")

        for row in range(3):

            print("| ", end="")
            print(" | ".join(self.board[row]), end="")
            print(" |")

    def display_board(self):
        for row in range(3):
            print("| ", end="")
            print(" | ".join(self.board[row]), end="")
            print(" |")

    def move(self, chosen_position):
        row = (chosen_position - 1) // 3
        col = (chosen_position - 1) % 3
        if self.turn == 1:
            current_sign = self.sign_one
        else:
            current_sign = self.sign_two
        self.board[row][col] = f"{current_sign}"
        self.turn = 1 if self.turn == 2 else 2
