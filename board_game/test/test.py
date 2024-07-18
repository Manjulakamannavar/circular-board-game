
### Tests
#### test_game.py
```python
import unittest
from game import Game
from player import Player
from board import Board
from dice import Dice

class TestGame(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
        self.board = Board("HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH", self.dice)
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.game = Game(self.board, self.player1, self.player
