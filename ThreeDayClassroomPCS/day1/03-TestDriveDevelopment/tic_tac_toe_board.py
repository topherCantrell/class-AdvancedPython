class TicTacToeBoard:

    def __init__(self):
        self._board = ['']*9

    def get_contents(self,cell):
        """
        Return the contents of the requested cell.
        :param cell: 0, 1, 2, 3, 4, 5, 6, 7, 8
        :return: 'X' or 'O' or '' (Empty)
        """        
        assert cell>=0 and cell<=8, 'Must be between 0 and 8'
        return self._board[cell]

    def clear(self):
        pass
    
    def make_move(self,cell,token):
        pass

    def get_status(self):
        pass

