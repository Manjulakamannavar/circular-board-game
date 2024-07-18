import random

class LoadedDice:
    def __init__(self):
        self.probabilities = [0.4, 0.2, 0.2, 0.2]
        self.outputs = [1, 2, 3, 'Roll Again']

    def roll(self):
        return random.choices(self.outputs, self.probabilities)[0]
