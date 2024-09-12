class PuzzlePiece:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape  # Shape is a 2D list representing the piece

    def display(self):
        for row in self.shape:
            print(' '.join(str(cell) for cell in row))
