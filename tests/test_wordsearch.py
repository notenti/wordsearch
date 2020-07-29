import unittest
from wordsearch import search


class TestWordSearch(unittest.TestCase):
    def test_find_all(self):
        board = search.Board(100, 100)
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))


if __name__ == '__main__':
    unittest.main()
