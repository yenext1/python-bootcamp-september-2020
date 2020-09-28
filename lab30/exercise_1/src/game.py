from time import sleep
from board import Board



class NonEvenCellsError(Exception):
    def __init__(self):
        super().__init__("You chose non even number of cells")


class Game:
    def __init__(self, player):
        self.player = player
        self.board = None
        while self.board is None:
            try:
                self.board = self.create_new_game()
            except NonEvenCellsError:
                print("Cell numbers (rows * columns) has to be even number")
            except ValueError:
                print("Input didn't match format, please try again (example 3,4)")
        self.start_game()

    def create_new_game(self):

        rows, columns = [int(i) for i in
                         input(f"{self.player.name}, choose number of rows/columns (format X,Y) ").split(
                             ',')]
        if rows * columns % 2 != 0:
            raise NonEvenCellsError
        return Board(rows, columns)


    def clear_screen(self):
        print("\n" * 100)

    def start_game(self):
        print("You have 5 second to memorize the board")
        sleep(2)
        self.board.present_board(show_letters=True)
        sleep(5)
        self.clear_screen()
        self.board.present_board(show_letters=False)
        while(self.is_game_ended() is False):
            self.player.next_move(self.board, self)
        print("Congratulations! You Won!")

    def is_game_ended(self):
        for r in range(len(self.board.hidden_board)):
            for c in range(len(self.board.hidden_board[r])):
                if self.board.hidden_board[r][c] == "*":
                    return False
        return True
