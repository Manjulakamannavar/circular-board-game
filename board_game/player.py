class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.balance = 5
        self.debt = 0
        self.miss_turn = False

    def update_balance(self, amount):
        self.balance += amount

    def update_debt(self, amount):
        self.debt += amount

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size

    def __str__(self):
        return f"{self.name}: Position={self.position}, Balance={self.balance}, Debt={self.debt}, MissTurn={self.miss_turn}"
