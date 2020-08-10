# Wordsearch

Small program that takes a list of words, attempts to fit them into a gameboard, and then searches for all the words that were placed.

## To use:

```python
from wordsearch import search

words_to_place = ['puppy', 'lemonade', 'knees', 'planter', 'twine']
board = search.Board(height = 10, width = 10, words_to_place)
ws = search.WordSearch(board)

for word in board.placed_words:
    if ws.search(word):
        print(f'Found {word}!')
```
