import collections
import random

class Board:
    def __init__(self, rows=3, columns=4):
        self.rows = rows
        self.columns = columns
        self.board = self.generate_new_board(rows, columns)
        self.hidden_board = self.generate_new_hidden_board(rows, columns)

    def generate_new_board(self, columns, rows):
        theabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        total_letters = []
        board = collections.defaultdict(list)
        for letter in range(columns * rows // 2):
            total_letters.extend([theabc[letter], theabc[letter]])
        for c in range(columns):
            for r in range(rows):
                selection = random.randint(0, len(total_letters) - 1)
                board[c].append(total_letters[selection])
                total_letters.pop(selection)
        return board

    def generate_new_hidden_board(self, columns, rows):
        hidden_board = [["*" for r in range(rows)] for c in range(columns)]
        return hidden_board

    def present_board(self, show_letters=True):
        for j in range(self.rows):
            for i in range(self.columns):
                print(f"{self.board[j][i] if show_letters else self.hidden_board[j][i]}  ", end="")
            print()
