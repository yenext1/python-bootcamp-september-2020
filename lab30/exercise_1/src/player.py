from time import sleep


class Player:
    def __init__(self):
        self.name = input("Hi, what is your name? ")

    def next_move(self, board, game):
        # It would have been better to have next_move return only one card
        # that way you can show the card every time it is selected,
        # and check if you have a pair when someone flips the second card
        # all inside the game class
        first = self.turn_card("first",board)
        second = self.turn_card("second",board)
        
        # The function next_move should focus on getting the next move from the user
        # and it'll be better to keep it clean from game logic
        # (so we'll be able to reuse it for other games)
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
