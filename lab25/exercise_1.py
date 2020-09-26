import collections
from random import randint
import re
import time
from typing import Literal


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def game_over(self, win, name):
        if win:
            self.score[name] += 10


class Board:
    def __init__(self):
        self.status = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    Sign = Literal["x", "o"]

    def change_status(self, x, y, sign: Sign):
        self.status[y][x] = sign
        self.print_board()

    def print_board(self):
        for i in range(len(self.status)):
            for j in range(len(self.status[i])):
                print(f"{self.status[i][j]:3}", end="")
            print()


class BasePlayer:

    def __init__(self, score_keeper):
        self.score = score_keeper

    def game_over(self, win):
        self.score.game_over(win, self.name)


class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Player"

    def next_move(self, board, msg=""):
        if msg:
            print(msg)
        cell = input(f"{self.name}, what's your next move? Type the square position (format X,Y) ")
        self.validate_move(cell, board)

    def validate_move(self, cell, board):
        pattern = re.compile(r'[1-3],[1-3]')
        if pattern.match(cell):
            x = int(cell.split(",")[0]) - 1
            y = int(cell.split(",")[1]) - 1
            if board.status[y][x] == ".":
                board.change_status(x, y, "x")
            else:
                self.next_move(board, "Oops, the cell you chose is not empty")
        else:
            self.next_move(board, "Oops, your input didn't match the format X,Y (for example type 1,3)")


class AIPlayer(BasePlayer):

    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Computer"

    def next_move(self, board):
        print("Computer is making its move")
        empty_cell = self.find_empty_cell(board)
        board.change_status(empty_cell[0], empty_cell[1], "o")

    @staticmethod
    def find_empty_cell(board):
        x = randint(0, 2)
        y = randint(0, 2)
        while board.status[y][x] != ".":
            x = randint(0, 2)
            y = randint(0, 2)
        return [x, y]


class Game:
    def __init__(self, name="Player", sk=Score()):
        self.score_keeper = sk
        self.h = HumanPlayer(self.score_keeper)
        self.h.name = name
        self.a = AIPlayer(self.score_keeper)
        self.board = Board()
        self.start_game()

    player1_turn = True

    def start_game(self):
        if self.h.name == "Player":
            name = input("What is your name? ")
            self.h.name = name
            time.sleep(1)
            print("In this tic-tac-toe game, you are x, the computer is o")
            time.sleep(0.5)
        player1 = self.choose_random_player()
        player2 = self.h if player1.name == "Computer" else self.a
        print(f"The first player is {player1.name}")
        self.play(player1, player2, self.board)

    def choose_random_player(self):
        coin_toss = randint(0, 1)
        return self.h if coin_toss else self.a

    def play(self, player1, player2, board):
        while not self.check_win(board):
            if self.player1_turn:
                player1.next_move(self.board)
                self.player1_turn = False
            else:
                player2.next_move(self.board)
                self.player1_turn = True
        if self.check_win(board) == "It's a tie":
            print("It's a tie")
            self.end_game()
        else:
            winner = player2 if self.player1_turn else player1
            print(f"{winner.name} won!")
            winner.score.game_over(True, winner.name)
            self.end_game()

    @staticmethod
    def check_win(board):
        for i in range(0, 3):
            if board.status[i][0] != "." and board.status[i][0] == board.status[i][1] == board.status[i][2]:
                return True

            elif board.status[0][i] != "." and board.status[0][i] == board.status[1][i] == board.status[2][i]:
                return True

            elif board.status[0][0] != "." and board.status[0][0] == board.status[1][1] == board.status[2][2]:
                return True

            elif board.status[0][2] != "." and board.status[0][2] == board.status[1][1] == board.status[2][0]:
                return True

        while '.' in [j for i in board.status for j in i]:
            return False
        return "It's a tie"

    def end_game(self):
        time.sleep(1)
        print(f"The score is {dict(self.a.score.score)}")
        time.sleep(0.5)
        print("Let's play another game")
        Game(self.h.name)


Game()
