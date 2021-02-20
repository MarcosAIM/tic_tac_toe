from tictactoe.board import BoardManager
from tictactoe.board import PositionError
from time import sleep
from tictactoe.player import player

#function for clearing command line
def clear():
    from os import system, name
    # windows
    if name == 'nt':
        _ = system('cls')
    # linux mac
    else:
        _ = system('clear')

#0 game in progress
#1 player one won
#2 player two won
#3 tie
class Game:
    def __init__(self):
        self.b_mng = BoardManager()
        self.game_state = 0

        self.player1 = [1,'X',player.player_input, []]
        self.player2 = [5,'O',player.player_input, []]

        self.player_turn = self.player1


    def game(self):
        input("Welcome to Tic-Tac-Toe. Press Enter to Play")
        clear()

        while self.game_state == 0:
            if self.b_mng.positions == False: #tie game
                self.game_state = 3
                break

            self.b_mng.print_board()

            try:
                row,col = self.player_turn[2](*self.player_turn[3])
                self.b_mng.place_move(row,col,self.player_turn[1])

            except IndexError:
                print("Row or Column out of range please try again......")
                sleep(1)
            except PositionError:
                print("Position filled. try again....")
                sleep(1)
            except ValueError:
                print("That's not a number try again.....")
                sleep(1)
            else:
                self.add_totals(row,col)
                self.check_win(row,col)
                self.switch_players()
            finally:
                clear()

        self.b_mng.print_board()
        print(f"Winner is:{self.game_state}")


    def switch_players(self):
        if self.player_turn[0] == 1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1

    def add_totals(self,row,col):
        self.b_mng.rows_totals[row] += self.player_turn[0]
        self.b_mng.cols_totals[col] += self.player_turn[0]
        pos = row * 3 + col

        if pos == 4:
            self.b_mng.diag_totals[0] += self.player_turn[0]
            self.b_mng.diag_totals[1] += self.player_turn[0]
        elif pos % 4 == 0:
            self.b_mng.diag_totals[0] += self.player_turn[0]
        elif pos % 2 == 0:
            self.b_mng.diag_totals[1] += self.player_turn[0]


    def check_win(self,row,col):
        w1 = self.player1[0] * 3
        w2 = self.player2[0] * 3
        if self.b_mng.rows_totals[row] == w1 or self.b_mng.cols_totals[col] == w1 or self.b_mng.diag_totals[0] == w1 or self.b_mng.diag_totals[1] == w1:
            self.game_state = self.player1[1]
        elif self.b_mng.rows_totals[row] == w2 or self.b_mng.cols_totals[col] == w2 or self.b_mng.diag_totals[0] == w2 or self.b_mng.diag_totals[1] == w2:
            self.game_state = self.player2[1]


    def set_player_func(self,func1,args1,func2,args2):
        self.player1[2] = func1
        self.player2[2] = func2
        self.player1[3] = args1
        self.player2[3] = args2
