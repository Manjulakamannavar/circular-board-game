import random

class LoadedDice:
    def roll(self):
        outcomes = [1, 2, 3, 'RollAgain']
        probabilities = [0.4, 0.2, 0.2, 0.2]
        result = random.choices(outcomes, weights=probabilities)[0]

        if result == 'RollAgain':
            return self.roll()
        else:
            return result
