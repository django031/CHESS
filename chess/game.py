from board import Board


class Game():
    def __init__(self):
        self.board = Board(8)
        self.board.print_board()

    def make_move(self, source_x, source_y, dest_x, dest_y, player_side):
        status = False
        if self.board.is_source_valid(source_x, source_y, player_side) and \
                self.board.is_dest_valid(dest_x, dest_y, player_side):
            piece = self.board.get_player_at_pos(source_x, source_y)
            status = piece.make_move(dest_x, dest_y, self.board)
            self.board.print_board()
        else:
            print("Invalid move.")
        return status

    def parse(self, iter):
        return [int(x) for x in iter.split(',')]


if __name__ == '__main__':
    obj = Game()
    player_side = 0
    while True:
        parsed_input = input("Enter move for player {} - ".format(str(player_side + 1))).split()
        if parsed_input[0] == "-1":
            print("Exiting.")
            break
        source, dest = parsed_input
        source_x, source_y = obj.parse(source)
        dest_x, dest_y = obj.parse(dest)
        print("Trying to move from ({}, {}) to ({}, {})".format(source_x, source_y, dest_x, dest_y))
        status = obj.make_move(source_x, source_y, dest_x, dest_y, player_side + 1)
        if status:
            player_side += 1
            player_side %= 2
        print(source_x, source_y, dest_x, dest_y)
