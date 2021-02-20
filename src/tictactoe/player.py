import random
from tictactoe.board import BoardManager

class PlayerStrategies:
    def __init__(self,bmg:BoardManager):
        self.modes = ['random', 'efficient','input']
        self.mode = self.modes[0]
        self.bmg = bmg

    def console_input(self):
        row = int(input("Enter Row:")) - 1
        col = int(input("Enter Column:")) - 1
        return row, col

    def random(self):
        return PlayerStrategies.pos_to_row_col(random.choice(self.bmg.positions))

    def efficient(self,*args):
        score = args[0] * 2
        opponent = args[1] * 2
        #check diagonals MY OWN SCORE OPPURTUNITY+++++++++++++++++
        lr = PlayerStrategies.check_for_potential_wins(score,self.bmg.diag_totals)
        if lr == 0:
            pos = self.check_for_positions(0,4,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        if lr == 1:
            pos = self.check_for_positions(2,4,6)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        #rows_totals
        lmr = PlayerStrategies.check_for_potential_wins(score,self.bmg.rows_totals)
        if lmr == 0:
            pos = self.check_for_positions(0,1,2)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        elif lmr == 1:
            pos = self.check_for_positions(3,4,5)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        elif lmr == 2:
            pos = self.check_for_positions(6,7,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        #cols_totals
        lmr = PlayerStrategies.check_for_potential_wins(score,self.bmg.cols_totals)
        if lmr == 0:
            pos = self.check_for_positions(0,3,6)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        elif lmr == 1:
            pos = self.check_for_positions(1,4,7)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        elif lmr == 2:
            pos = self.check_for_positions(2,5,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        #check diagonals OPPONENTS OPPURTUNITY+++++++++++++++++
        lr = PlayerStrategies.check_for_potential_wins(opponent,self.bmg.diag_totals)
        if lr == 0:
            pos = self.check_for_positions(0,4,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        if lr == 1:
            pos = self.check_for_positions(2,4,6)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        #rows_totals
        lmr = PlayerStrategies.check_for_potential_wins(opponent,self.bmg.rows_totals)
        if lmr == 0:
            pos = self.check_for_positions(0,1,2)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        if lmr == 1:
            pos = self.check_for_positions(3,4,5)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        if lmr == 2:
            pos = self.check_for_positions(6,7,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        #cols_totals
        lmr = PlayerStrategies.check_for_potential_wins(opponent,self.bmg.cols_totals)
        if lmr == 0:
            pos = self.check_for_positions(0,3,6)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)
        if lmr == 1:
            pos = self.check_for_positions(1,4,7)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        if lmr == 2:
            pos = self.check_for_positions(2,5,8)
            if pos != -1:
                return PlayerStrategies.pos_to_row_col(pos)

        # NO THREATS +++++++++++++++++++++++++++++++++++++++++++++++++++++
        pos = self.check_for_positions(4,0,2,6,8)
        if pos != -1:
            return PlayerStrategies.pos_to_row_col(pos)
        pos = self.check_for_positions(1,3,5,7,)
        if pos != -1:
            return PlayerStrategies.pos_to_row_col(pos)


    def check_for_positions(self,*positions):
        for num in positions:
            if num in self.bmg.positions:
                return num
        return -1


    def check_for_potential_wins(score,totals):
        for num,total in enumerate(totals):
            if score == total:
                return num
        return -1

    def pos_to_row_col(pos):
        row = pos // 3
        col = pos - (row * 3)
        return row, col
