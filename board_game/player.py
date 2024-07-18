class Player:
    def __init__(self, name):
        self.name = name
        self.balance = 5
        self.debt = 0
        self.position = 0  # Start position on the board
        self.miss_turn = False  # Flag to skip next turn if on Jail square

    def update_balance(self, amount):
        self.balance += amount

    def update_debt(self, amount):
        self.debt += amount

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size

    def __str__(self):
        return f"{self.name}: Balance - {self.balance}, Debt - {self.debt}"
