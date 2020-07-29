import unittest
import os
from wordsearch import search


class TestWordSearch(unittest.TestCase):
    def test_find_all(self):

        current_loc = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(current_loc, 'common_words.txt')

        with open(filename) as f:
            wordlist = f.read().splitlines()

        board = search.Board(100, 100, wordlist)
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))


if __name__ == '__main__':
    unittest.main()
