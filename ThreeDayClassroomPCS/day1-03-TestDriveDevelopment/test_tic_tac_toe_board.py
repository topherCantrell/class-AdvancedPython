# https://docs.python.org/3/library/unittest.html

import unittest

from tic_tac_toe_board import TicTacToeBoard

class TestTicTacToeBoard(unittest.TestCase):
        
    def tearDown(self):
        pass
    
    def setUp(self):
        self.board = TicTacToeBoard()

    def test_board_starts_clear(self):        
        for cell in range(9):
            self.assertTrue(self.board.get_contents(cell)=='')
            
    def test_get_invalid_cells(self):
        board = TicTacToeBoard()          
        with self.assertRaises(AssertionError) as cm:  
            board.get_contents(9)
        self.assertTrue(str(cm.exception)=='Must be between 0 and 8')
        with self.assertRaises(AssertionError) as cm: 
            board.get_contents(-1)            
        self.assertTrue(str(cm.exception)=='Must be between 0 and 8')

    def test_making_move(self):
        pass

    def test_making_move_to_taken_cell(self):
        pass

    def test_x_wins(self):
        pass
