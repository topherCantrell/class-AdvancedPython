import tictactoe
import unittest

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = tictactoe.TicTacToeBoard()

    def tearDown(self):
        pass

    def test_good_move(self):
        self.board.make_move(0,'X')
        c = self.board.get_cell(0)
        self.assertTrue(c=='X')

    def test_bad_token(self):
        with self.assertRaises(AssertionError):
            self.board.make_move(0,'Z')

    def test_bad_cell(self):
        with self.assertRaises(AssertionError):
            self.board.make_move(-7,'Z')

    def test_o_wins(self):
        self.board.make_move(0, 'X')
        self.board.make_move(3, 'O')
        self.board.make_move(1, 'X')
        self.board.make_move(4, 'O')
        self.board.make_move(8, 'X')
        self.board.make_move(5, 'O')
        self.assertTrue(self.board.get_status()=='O Wins')