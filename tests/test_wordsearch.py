from typing import List
import unittest
import os
from wordsearch import search


class TestWordSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.words = generateWordlist('common_words.txt')

    def test_one_word_small_board(self):
        one_word = self.words[50]
        board = search.Board(10, 10, [one_word])
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))

    def test_many_words_small_board(self):
        many_words = self.words[40:60]
        board = search.Board(10, 10, many_words)
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))

    def test_one_word_large_board(self):
        one_word = self.words[-2]
        board = search.Board(500, 500, [one_word])
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))

    def test_many_words_large_board(self):
        many_words = self.words[100:600]
        board = search.Board(500, 500, many_words)
        ws = search.WordSearch(board)

        for word in board.placed_words:
            self.assertTrue(ws.search(word))


def generateWordlist(filename: str) -> List[str]:

    current_loc = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_loc, filename)

    with open(filename) as f:
        return f.read().splitlines()


if __name__ == '__main__':
    unittest.main()
