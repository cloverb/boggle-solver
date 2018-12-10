import os
from error import InvalidBoardError


class Board:
    """Boggle board representation"""

    def __init__(self, file):
        self.cells = []
        with open(file) as f:
            for line in f:
                if not line.rstrip(os.linesep).replace(' ', '').isalpha():
                    raise InvalidBoardError
                letters = line.split()
                if self.cells and len(letters) != len(self.cells[-1]):
                    raise InvalidBoardError
                self.cells.append(letters)
        if not self.cells:
            raise InvalidBoardError
        self.rows = len(self.cells)
        self.cols = len(self.cells[0])

    def get(self, row, col):
        """Get letter at position (row, col)"""
        return self.cells[row][col]
