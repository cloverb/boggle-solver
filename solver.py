from nltk.corpus import words
from trie import Trie


class Solver:
    """Boggle board solver"""

    MIN_WORD_LENGTH = 3

    def __init__(self):
        self.dictionary = Trie()
        for word in words.words():
            self.dictionary.insert(word)

    def solve(self, board):
        """Solve boggle board with modified depth-first search"""
        results = set()
        visited = [[False for x in range(board.cols)] for y in range(board.rows)]
        for row in range(board.rows):
            for col in range(board.cols):
                self.search(board, row, col, visited, results, '')
        return results

    def search(self, board, row, col, visited, results, prefix):
        """Modified depth-first search which short-circuits for invalid prefixes"""
        if not self.dictionary.search_prefix(prefix):
            return

        visited[row][col] = True

        word = prefix + board.get(row, col)
        if len(word) >= self.MIN_WORD_LENGTH and self.dictionary.search_word(word):
            results.add(word)

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < board.rows and 0 <= j < board.cols and not visited[i][j]:
                    self.search(board, i, j, visited, results, word)

        visited[row][col] = False
