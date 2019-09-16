from player import Rook, Knight, Queen, Bishop, King, Pawn, Blank


class Board(object):

    def __init__(self, board_size):
        self.n = board_size
        self.board = [[Blank()]*self.n for i in range(self.n)]
        self.init_board()

    def print_board(self):
        for i in range(self.n):
            print("\t", end="")
            for j in range(self.n):
                print(self.board[i][j], "   ", end="", sep='')
            print("")

    def is_dest_valid(self, x, y, player_side):
        dest_player = self.get_player_at_pos(x, y)
        return self._within_board(x) and \
               self._within_board(y) and \
               dest_player.player_side != player_side

    def is_source_valid(self, x, y, player_side):
        current_player = self.get_player_at_pos(x, y)
        return current_player is not Blank and \
               self._within_board(x) and \
               self._within_board(y) and \
               current_player.player_side == player_side

    def _within_board(self, x):
        if 0 <= x < self.n:
            return True

    def get_player_at_pos(self, x, y):
        return self.board[x][y]

    def update(self, piece, source_x, source_y, dest_x, dest_y):
        self.board[dest_x][dest_y] = piece
        self.board[source_x][source_y] = Blank(source_x, source_y, 0)

    def init_board(self):
        for i in range(self.n):
            self.board[1][i] = Pawn(1,i,1)
            self.board[self.n-2][i] = Pawn(self.n-2,i,2)
        for i,each in enumerate([Rook, Knight, Bishop, King, Queen]):
            self.board[0][i] = each(0,i,1)
            self.board[0][self.n-1-i] = each(0,self.n-1-i,1)
            self.board[self.n-1][i] = each(self.n-1,i,2)
            self.board[self.n-1][self.n-1-i] = each(self.n-1,self.n-1-i,2)
        for i in range(2,self.n-2):
            for j in range(self.n):
                self.board[i][j] = Blank(i,j,0)
        self.board[0][4] = King(0,4,1)
        self.board[self.n - 1][3] = King(self.n - 1,3,2)


if __name__ == '__main__':
    obj = Board(8)
    obj.print_board()
