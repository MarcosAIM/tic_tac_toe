class Board:
    def __init__(self):
        self.board = (['_','_','_'],['_','_','_'],['_','_','_'])

class PositionError(Exception):
    pass

class BoardManager:
    def __init__(self):
        self.board = Board()
        self.rows_totals = [0,0,0]
        self.cols_totals = [0,0,0]
        self.diag_totals = [0,0]
        self.positions = [0,1,2,3,4,5,6,7,8]

    def print_board(self):
        print("  1|2|3")
        for row,arr in enumerate(self.board.board):
            print(row+1,end='|')
            print('|'.join([*arr]))

    def place_move(self,row,col,player_grph):
        if self.board.board[row][col] == '_':
            self.board.board[row][col] = player_grph
            pos = row * 3 + col
            self.positions.remove(pos)
        else:
            raise PositionError
