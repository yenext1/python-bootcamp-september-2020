class ParseMoveError(Exception):
    def __init__(self):
        super().__init__("Sorry")


def try_to_read_move_from_player(player_name):
    if player_name != "Moses":
        raise ParseMoveError

try:
    try_to_read_move_from_player("Mose")
except ParseMoveError as err:
    print(err)