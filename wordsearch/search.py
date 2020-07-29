from typing import List, Tuple
import random

Location = Tuple[int, int]


class Board:
    def __init__(self, height: int, width: int, wordlist: List[str]) -> None:
        self.height = height
        self.width = width
        self.wordlist = wordlist
        self.visited = [[False] * self.width for _ in range(self.height)]
        self.placed_words = []
        self.board = [[''] * self.width for _ in range(self.height)]
        self.__populateBoard()

    def __populateBoard(self) -> None:
        for word in self.wordlist:
            open_spaces = self.__findWordLocation(word)

            if len(open_spaces) == len(word):
                self.placed_words.append(word)

            self.__placeOnBoard(open_spaces, word)

        alpha = 'thequickbrownfoxjumpsoverthelazydog'
        for i in range(self.height):
            for j in range(self.width):
                if not self.board[i][j]:
                    self.board[i][j] = random.choice(alpha)

    def __findWordLocation(self, word: str) -> List[Location]:
        valid_loc = self.__generateValidStartLocation()
        spaces = []
        max_placement_attempts = 10
        placement_attempts = 0
        while not self.__canPlace(word, valid_loc, spaces) and placement_attempts < max_placement_attempts:
            placement_attempts += 1
            valid_loc = self.__generateValidStartLocation()
            spaces.clear()
        return spaces

    def __generateValidStartLocation(self) -> Location:
        i, j = random.randrange(self.height), random.randrange(self.width)
        while self.visited[i][j]:
            i, j = random.randrange(self.height), random.randrange(self.width)
        return (i, j)

    def __canPlace(self, word: str, start_location: Location, spaces: List[Location]) -> bool:
        self.__searchSpaces(word, start_location, spaces)

        if len(spaces) == len(word):
            return True
        for loc in spaces:
            i, j = loc
            self.visited[i][j] = False
        return False

    def __searchSpaces(self, word: str, loc: Location, spaces: List[Location]) -> None:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        stack = [loc]
        while stack and len(spaces) < len(word):
            random.shuffle(dirs)
            i, j = stack.pop()
            spaces.append((i, j))
            self.visited[i][j] = True
            k = 0
            while k < len(dirs) and not self.__isValidMove(i + dirs[k][0], j + dirs[k][1]):
                k += 1
            if k == len(dirs):
                break
            next_loc = (i + dirs[k][0], j + dirs[k][1])
            stack.append(next_loc)

    def __isValidMove(self, i: int, j: int) -> bool:
        if 0 <= i < self.height and 0 <= j < self.width and not self.visited[i][j]:
            return True
        return False

    def __placeOnBoard(self, spaces: List[Location], word: str) -> None:
        for idx, space in enumerate(spaces):
            i, j = space
            self.board[i][j] = word[idx]

    def __getitem__(self, index):
        return self.board[index]

    def __len__(self):
        return len(self.board)


class WordSearch:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.visited = [[False] * len(self.board[0])
                        for _ in range(len(self.board))]

    def search(self, word: str) -> bool:
        if not word:
            return False

        for i in range(self.board.height):
            for j in range(self.board.width):
                if self.board[i][j] == word[0]:
                    if self.__dfs(word, 0, i, j):
                        return True
        return False

    def __dfs(self, word: str, idx: int, i: int, j: int):
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i == len(self.board) or j == len(self.board[0]):
            return False
        if self.visited[i][j] or self.board[i][j] != word[idx]:
            return False

        self.visited[i][j] = True
        exist = self.__dfs(word, idx+1, i+1, j) or  \
            self.__dfs(word, idx+1, i-1, j) or \
            self.__dfs(word, idx+1, i, j+1) or \
            self.__dfs(word, idx+1, i, j-1)
        self.visited[i][j] = False
        return exist
