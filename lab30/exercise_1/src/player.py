from time import sleep


class Player:
    def __init__(self):
        # self.name = input("Hi, what is your name? ")
        self.name = "Yonatan"

    def next_move(self, board, game):
        first = self.turn_card("first",board)
        second = self.turn_card("second",board)
        print(f"first: {first}, second {second}")
        if first == second:
            self.flip(first,board)
        else:
            board.present_board(show_letters=True)
            sleep(1)
            game.clear_screen()
        board.present_board(show_letters=False)

    def turn_card(self, order ,board):
        card = None
        while card is None:
            try:
                card = input(f"What is the {order} card to turn (format X,Y)?")
                x, y = [int(i) - 1 for i in card.split(',')]
                return board.board[x][y]
            except IndexError:
                print(f"[{x+1},{y+1}] is not in the board range")
            except ValueError:
                print("The input is not in the right format (X,Y)")



    def flip(self,letter,board):
        for r in range(len(board.board)):
            for c in range(len(board.board[r])):
                if board.board[r][c] == letter:
                    board.hidden_board[r][c] = letter
