import collections
from random import randint


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def game_over(self, win, name):
        if win:
            self.score[name] += 10


class Board:
    def __init__(self):
        self.status = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def change_status(self, x, y, sign):
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
        self.name = "Joe"

    def next_move(self, board):
        cell = input("What's your next move? Type the square position (format X,Y) ")
        x = int(cell.split(",")[0])-1
        y = int(cell.split(",")[1])-1
        board.change_status(x, y, "x")


class AIPlayer(BasePlayer):

    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Computer"

    def next_move(self, board):
        print("Computer is making its move")
        empty_cell = self.find_empty_cell(board)
        board.change_status(empty_cell[0], empty_cell[1], "o")

    def find_empty_cell(self, board):
        x = randint(0, 2)
        y = randint(0, 2)
        while board.status[y][x] != ".":
            x = randint(0, 2)
            y = randint(0, 2)
        return [x,y]


class Game:

    def __init__(self):
        self.score_keeper = Score()
        self.h = HumanPlayer(self.score_keeper)
        self.a = AIPlayer(self.score_keeper)
        self.board = Board()
        self.start_game()

    player1_turn = True

    def start_game(self):
        name = input("What is your name? ")
        self.h.name = name
        print("You are x")
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
                self.player1_turn= False
            else:
                player2.next_move(self.board)
                self.player1_turn = True
        if self.check_win(board)=="It's a tie":
            print("It's a tie")
            new_game = Game()
        else:
            winner = player2 if(self.player1_turn) else player1
            print(f"{winner.name} won!")
            winner.score.game_over(True, winner.name)
            print(self.a.score.score)
            new_game = Game()


    def check_win(self, board):
        for i in range(0,2):
            if board.status[i][0] != "." and board.status[i][0] == board.status[i][1] == board.status[i][2]:
                return True

            elif board.status[0][i] != "." and board.status[0][i] == board.status[1][i] == board.status[2][i]:
                return True

            elif board.status[0][0] != "." and board.status[0][0] == board.status[1][1] == board.status[2][2] != ".":
                return True

            elif board.status[0][2] != "." and board.status[0][2] == board.status[1][1] == board.status[2][0] != ".":
                return True

        while '.' in [j for i in board.status for j in i]:
            return False
        return "It's a tie"


new_game = Game()
