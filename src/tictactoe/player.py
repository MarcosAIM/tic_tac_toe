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
        pos = random.choice(self.bmg.positions)
        row = pos // 3
        col = pos - (row * 3)
        return row, col

    def efficient(self):
        pass
