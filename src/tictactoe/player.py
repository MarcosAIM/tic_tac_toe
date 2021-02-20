import random


class player:
    def __init__(self):
        self.modes = ['random', 'efficient','input']
        self.mode = self.modes[0]

    def player_input():
        row = int(input("Enter Row:")) - 1
        col = int(input("Enter Column:")) - 1
        return [row,col]

    def random(*positions):
        pos = random.choice(positions)
        row = pos // 3
        col = pos - (row * 3)
        return row, col
