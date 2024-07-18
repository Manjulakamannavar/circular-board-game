class Board:
    def __init__(self, layout):
        self.layout = layout

    def get_square_type(self, position):
        return self.layout[position]
