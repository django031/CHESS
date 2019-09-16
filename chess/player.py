from abc import abstractmethod


class BasePlayer(object):
    def __init__(self, x="x", y="x", player_side=0):
        self.pos_x = x
        self.pos_y = y
        self.player_side = player_side

    def make_move(self, dest_x, dest_y, board):
        status = False
        if self.is_valid(dest_x, dest_y, board.board):
            self.update(board, dest_x, dest_y)
            status = True
        else:
            print("Invalid move for {}".format(str(self)))
        return status

    def is_valid(self, dest_x, dest_y, board):
        valid_moves = self.get_moves(len(board), board)
        if (dest_x, dest_y) in valid_moves:
            if board[dest_x][dest_y].__class__ == Blank:
                return 1
            elif board[dest_x][dest_y].player_side != self.player_side:
                return 1
        else:
            return 0

    def update(self, board, dest_x, dest_y):
        board.update(self, self.pos_x, self.pos_y, dest_x, dest_y)
        self.pos_x = dest_x
        self.pos_y = dest_y


class Blank(BasePlayer):
    def __str__(self):
        return "____-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)


class Rook(BasePlayer):
    def __str__(self):
        return "Rook-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def get_moves(self, n, board):
        valid_moves = []
        for type in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            xtemp, ytemp = self.pos_x + type[0], self.pos_y + type[1]
            while 0 <= xtemp < n and 0 <= ytemp < n:
                if board[xtemp][ytemp].__class__ == Blank:
                    break
                valid_moves.append((xtemp, ytemp))
                xtemp, ytemp = xtemp + type[0], ytemp + type[1]
        return valid_moves


class King(BasePlayer):
    def __str__(self):
        return "King-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def get_moves(self, n, board=None):
        return [(self.pos_x+1,self.pos_y),(self.pos_x+1,self.pos_y+1),(self.pos_x+1,self.pos_y-1),(self.pos_x,self.pos_y+1),(self.pos_x,self.pos_y-1),(self.pos_x-1,self.pos_y),(self.pos_x-1,self.pos_y+1),(self.pos_x-1,self.pos_y-1)]


class Queen(BasePlayer):
    def __str__(self):
        return "Quee-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def get_moves(self, n, board):
        valid_moves = []
        for type in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            xtemp, ytemp = self.pos_x + type[0], self.pos_y + type[1]
            while 0 <= xtemp < n and 0 <= ytemp < n:
                if board[xtemp][ytemp].__class__ != Blank:
                    break
                valid_moves.append((xtemp, ytemp))
                xtemp, ytemp = xtemp + type[0], ytemp + type[1]
        for type in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            xtemp, ytemp = self.pos_x + type[0], self.pos_y + type[1]
            while 0 <= xtemp < n and 0 <= ytemp < n:
                if board[xtemp][ytemp].__class__ != Blank:
                    break
                valid_moves.append((xtemp, ytemp))
                xtemp, ytemp = xtemp + type[0], ytemp + type[1]
        return valid_moves


class Bishop(BasePlayer):
    def __str__(self):
        return "Bish-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def get_moves(self, n, board):
        valid_moves = []
        for type in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            xtemp, ytemp = self.pos_x + type[0], self.pos_y + type[1]
            while 0 <= xtemp < n and 0 <= ytemp < n:
                if board[xtemp][ytemp].__class__ == Blank:
                    break
                valid_moves.append((xtemp, ytemp))
                xtemp, ytemp = xtemp + type[0], ytemp + type[1]
        return valid_moves


class Knight(BasePlayer):
    def __str__(self):
        return "Kngh-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def get_moves(self, n, board=None):
        return [(self.pos_x + 2, self.pos_y + 1), (self.pos_x - 2, self.pos_y + 1),
         (self.pos_x + 2, self.pos_y - 1), (self.pos_x - 2, self.pos_y - 1),
         (self.pos_x + 1, self.pos_y + 2), (self.pos_x - 1, self.pos_y + 2),
         (self.pos_x + 1, self.pos_y - 2), (self.pos_x - 1, self.pos_y - 2)]


class Pawn(BasePlayer):
    def __str__(self):
        return "Pawn-{}({},{})".format(self.player_side, self.pos_x, self.pos_y)

    def is_valid(self, dest_x, dest_y, board):
        stride = 1 if self.player_side == 1 else -1
        if self.pos_x + stride == dest_x and self.pos_y == dest_y and board[dest_x][dest_y].__class__ == Blank:
            return 1
        elif self.pos_x + stride == dest_x and self.pos_y + stride == dest_y and board[dest_x][dest_y].__class__ != Blank and board[dest_x][dest_y].player_side != self.player_side:
            return 1
        elif self.pos_x + stride == dest_x and self.pos_y + stride == dest_y and board[dest_x][dest_y].__class__ != Blank and board[dest_x][dest_y].player_side != self.player_side:
            return 1
        else:
            return 0
