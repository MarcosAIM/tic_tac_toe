class Board:
    def __init__(self):
        self.board = (['_','_','_'],['_','_','_'],['_','_','_'])

class BoardManager:
    def __init__(self):
        self.board = Board()
        self.rows_totals = [0,0,0]
        self.cols_totals = [0,0,0]
        self.diag_totals = [0,0]

    def print_board(self):
        for row in self.board.board:
            print('|'.join([*row]))

    def place_move(self,row,col,player_grph):
            self.board.board[row][col] = player_grph

    def show_move(self,row,col,player_grph):
        self.board.board[row][col] = player_grph
        self.print_board()
        self.board.board[row][col] = '_'

def main():
    bm = BoardManager()
    bm.show_move(1,2)
    bm.print_board()
    bm.place_move(1,2)
    bm.print_board()


if __name__ == '__main__':
    main()
