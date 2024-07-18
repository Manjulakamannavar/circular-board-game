from player import Player
from board import Board
from dice import LoadedDice

class Game:
    def __init__(self, board_layout, player_names):
        self.board = Board(board_layout)
        self.players = [Player(name) for name in player_names]
        self.dice = LoadedDice()
        self.current_player_index = 0

    def next_turn(self):
        player = self.players[self.current_player_index]

        if player.miss_turn:
            player.miss_turn = False
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            return

        roll_result = self.dice.roll()
        player.move(roll_result, len(self.board.layout))
        square_type = self.board.get_square_type(player.position)

        self.handle_square(square_type, player)
        self.check_win_condition(player)

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def handle_square(self, square_type, player):
        if square_type == 'B':  # Bank
            player.update_balance(10)
            # Player can take loan or repay (assumed functionality)

        elif square_type == 'J':  # Jail
            player.update_balance(-20)
            player.miss_turn = True

        elif square_type == 'H':  # House
            if player.balance > 0:
                player.update_balance(2)
            else:
                player.update_balance(-2)
            if player.debt > 0:
                player.update_debt(1)

    def check_win_condition(self, player):
        for opponent in self.players:
            if opponent != player:
                if player.balance - player.debt > 100:
                    print(f"{player.name} wins!")
                    exit()
                elif opponent.debt - opponent.balance > 100:
                    print(f"{player.name} wins because {opponent.name} has too much debt!")
                    exit()

    def display_board(self):
        for i, square in enumerate(self.board.layout):
            player_positions = [player.name[0] if player.position == i else '.' for player in self.players]
            print(f"{square} [{' '.join(player_positions)}]")

    def display_status(self):
        for player in self.players:
            print(player)
