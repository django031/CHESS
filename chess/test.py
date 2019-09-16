import unittest

from board import Board


class ChessTestMethods(unittest.TestCase):

    def setUp(self):
        self.board_obj = Board(8)

    # Board test cases
    def test_get_player_at_pos(self):
        self.assertEqual(self.board_obj.get_player_at_pos(0,0), self.board_obj.board[0][0])

    def test_init_board(self):
        rook_position = "Rook-1(0,0)"
        self.assertEqual(str(self.board_obj.board[0][0]), rook_position)

        knight_position = "Kngh-1(0,1)"
        self.assertEqual(str(self.board_obj.board[0][1]), knight_position)

    def test_is_dest_value(self):
        self.assertFalse(self.board_obj.is_dest_valid(-1,2,1))

    def test_is_source_value(self):
        self.assertFalse(self.board_obj.is_source_valid(-1, 2, 1))


if __name__ == '__main__':
    unittest.main()
