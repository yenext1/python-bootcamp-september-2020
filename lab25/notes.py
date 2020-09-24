import collections

class BoardUtils:
    def scan_board(self, board, code_to_run_for_each_item):
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board[i]) - 1)
                if res is not None:
                    return res

class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def game_over(self, win, name):
        if win:
            self.score[name] += 10


class BasePlayer:

    def __init__(self, score_keeper):
        self.score = score_keeper

    def game_over(self, win):
        self.score.game_over(win, self.name)


class HumanPlayer(BasePlayer):
    def __init__(self,score_keeper):
        super().__init__(score_keeper)
        self.name = "Joe"

    def next_move(self, board):
        self.print_board(board)
        next_move = input("What's your next move? Type the square position")
        return next_move

    def print_board(self, board):
        utils = BoardUtils()
        utils.scan_board(
            board,
            lambda i, j, is_last: print(
                f"{board[i][j]:3}", end="\n" if is_last else ""
            )
        )


class AIPlayer(BasePlayer):

    def __init__(self,score_keeper):
        super().__init__(score_keeper)
        self.name = "Bot"

    def next_move(self, board):
        def foreach_cell(i, j, is_last):
            if board[i][j] == ".":
                return f"{j}, {i}"

        utils = BoardUtils()
        return utils.scan_board(
            board,
            foreach_cell,
        )


score_keeper = Score()
h = HumanPlayer(score_keeper)
a = AIPlayer(score_keeper)
board = [['x','.','.'],['o','.','.'],['.','.','.']]
h.next_move(board)


print(a.score.score)
