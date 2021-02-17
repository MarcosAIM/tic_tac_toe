from tictactoe.board import BoardManager

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

        self.player1 = [1,'X']
        self.player2 = [5,'O']
        self.player_turn = self.player1

    def game(self):
        print("Welcome to Tic-Tac-Toe. Press Enter to Play")
        input()
        clear()

        while self.game_state == 0:
            self.b_mng.print_board()
            row = int(input("Enter Row:")) - 1
            col = int(input("Enter Column:")) - 1

            self.b_mng.place_move(row,col,self.player_turn[1])
            self.b_mng.print_board()
            self.add_totals(row,col)
            self.check_win(row,col)
            self.switch_players()
            clear()

        print(f"Winner is:{self.game_state}")



    def switch_players(self):
        if self.player_turn[0] == 1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1


    def add_totals(self,row,col):
        self.b_mng.rows_totals[row] += self.player_turn[0]
        self.b_mng.cols_totals[col] += self.player_turn[0]

        if (row + col) % 4 == 0:
            self.b_mng.diag_totals[0] += self.player_turn[0]
        elif (row + col) % 2 == 0:
            self.b_mng.diag_totals[1] += self.player_turn[0]

    def check_win(self,row,col):
        w1 = self.player1[0] * 3
        w2 = self.player2[0] * 3
        if self.b_mng.rows_totals[row] == w1 or self.b_mng.cols_totals[col] == w1 or self.b_mng.diag_totals[0] == w1 or self.b_mng.diag_totals[1] == w1:
            self.game_state = self.player1[1]
        elif self.b_mng.rows_totals[row] == w2 or self.b_mng.cols_totals[col] == w2 or self.b_mng.diag_totals[0] == w2 or self.b_mng.diag_totals[1] == w2:
            self.game_state = self.player2[1]
