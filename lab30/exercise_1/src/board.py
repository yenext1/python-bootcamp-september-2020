import collections
import random
import string

class Board:
    def __init__(self, rows=3, columns=4):
        self.rows = rows
        self.columns = columns
        self.board = self.generate_new_board(rows, columns)
        self.hidden_board = self.generate_new_hidden_board(rows, columns)

    def generate_new_board(self, columns, rows):
        # Python already has this:
        theabc = string.ascii_letters
        # theabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        board = collections.defaultdict(list)
        # Let's talk about this loop:
        # total_letters = []
        # for letter in range(columns * rows // 2):
        #     total_letters.extend([theabc[letter], theabc[letter]])
        # 
        # You're building a list out of SOMETHING
        # this patterns has a name - list comprehension
        # so this same code can be written using this:
        total_letters = [[theabc[letter], theabc[letter]] for letter in range(columns * rows // 2)]

        # But actually we can make this selection more interesting using random:
        total_letters = [[letter, letter] for letter in random.sample(theabc, k=(columns * rows // 2))]

        # And another by-the-way here. Using numpy to represent 2D arrays can give us a nicer
        # code when creating the board. Check this out:

        # board = np.random.choice(
        #         np.array(total_letters).flatten(),
        #         replace=False,
        #         size=columns * rows,
        # ).reshape(rows, columns)

        for c in range(columns):
            for r in range(rows):
                selection = random.randint(0, len(total_letters) - 1)
                board[c].append(total_letters[selection])
                total_letters.pop(selection)
        return board

    def generate_new_hidden_board(self, columns, rows):
        # Again with numpy that would have been:
        # hidden_board = np.full(fill_value='*', shape=(rows, columns))

        hidden_board = [["*" for r in range(rows)] for c in range(columns)]
        return hidden_board

    def present_board(self, show_letters=True):
        for j in range(self.rows):
            for i in range(self.columns):
                print(f"{self.board[j][i] if show_letters else self.hidden_board[j][i]}  ", end="")
            print()
