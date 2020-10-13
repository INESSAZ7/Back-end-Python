class TicTacGame:

    def __init__(self):
        self.cells = list(range(0, 10))
        self.curr_player = ' '
        self.number_of_moves = 0

    def show_board(self):
        print('\t _________________')
        for i in range(3):
            print("\t|     |     |     |")
            print("\t| {}   |  {}  |  {}  |".format(self.cells[1+i*3],
                                                    self.cells[2+i*3],
                                                    self.cells[3+i*3]))
            print('\t|_____|_____|_____|')
        print("\n")

    def choice_symbol(self):
        self.curr_player = input("Choice 'X' or 'O' ...\n")
        if self.curr_player == 'X' or self.curr_player == 'O':
            return True

        else:
            print("Incorrect answer! Try again\n")
            return False

    def validate_input(self, ans):
        try:
            ans = int(ans)

        except ValueError:
            print("Incorrect input! This is not a number. "
                  "Try again!")
            return False

        if 1 <= ans <= 9:
            if str(self.cells[ans]) not in "XO":
                self.cells[ans] = self.curr_player
                return True
            else:
                print("That cell is already filled!")
                return False

        else:
            print("Incorrect input! Input a number from 1 to 9. "
                  "Try again!")
            return False

    def change_player(self):
        if self.curr_player == 'X':
            self.curr_player = 'O'
        else:
            self.curr_player = 'X'

    def check_winner(self):
        win_comb = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                    (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for x in win_comb:
            if self.cells[x[0]] == self.cells[x[1]] == self.cells[x[2]]:
                return self.cells[x[0]]
        return False

    def start_game(self):

        end = False
        valid = False
        while not valid:
            valid = self.choice_symbol()

        while not end:
            self.show_board()
            valid = False
            while not valid:
                ans = input("Your turn, player " +
                            self.curr_player +
                            ". Which cell?\n")
                valid = self.validate_input(ans)

            self.number_of_moves += 1

            if self.number_of_moves > 4:
                player = self.check_winner()
                if player:
                    print(player, " win! \nGame Over.\n")
                    break

            if self.number_of_moves == 9:
                print("Tie! \nGame Over.\n")
                break

            self.change_player()

        self.show_board()


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
