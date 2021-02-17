from board import BoardManager

#function for clearing command line
def clear():
    from os import system, name
    # windows
    if name == 'nt':
        _ = system('cls')
    # linux mac
    else:
        _ = system('clear')



class Game:
    def __init__(self):
        self.b_mng = BoardManager()
        self.game_state = 0

        self.player1 = 1
        self.player2 = 5
        self.player_turn = self.player1

        self.player1_grph = 'X'
        self.player2_grph = 'O'

    def game(self):
        print("Welcome to Tic-Tac-Toe. Press Enter to Play")
        input()
        clear()
        self.b_mng.print_board()

        x = input()

        while x != '':

            x = input()

    def add_totals(self,row,col):
        self.b_mng.rows_totals[row] += self.player_turn
        self.b_mng.cols_totals[col] += self.player_turn

        if (row + col) % 4 == 0:
            self.b_mng.diag_totals[0] += self.player_turn
        elif (row + col) % 2 == 0:
            self.b_mng.diag_totals[1] += self.player_turn

    def check_win(self,row,col):
        w1 = self.player1 * 3
        w2 = self.player2 * 3
        if self.b_mng.rows_totals[row] == w1 or self.b_mng.cols_totals[col] == w1 or self.b_mng.diag_totals[0] == w1 or self.b_mng.diag_totals[1] == w1:
            self.game_state = 1
        elif self.b_mng.rows_totals[row] == w2 or self.b_mng.cols_totals[col] == w2 or self.b_mng.diag_totals[0] == w2 or self.b_mng.diag_totals[1] == w2:
            self.game_state = 2


def main():
    g = Game()
    g.game()


if __name__ == '__main__':
    main()
