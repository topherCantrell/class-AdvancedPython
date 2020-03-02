
"""

0 1 2
3 4 5
6 7 8

'' = empty
'X' = X
'O' = O

'X wins'
'O wins'
'Tie'
'Playing'

"""

WINS = [ [0,1,2],
         [3,4,5],
         [6,7,8],
         [0, 3, 6],
         [1, 4, 7],
         [2, 5, 8],
         [0, 4, 8],
         [2, 4, 6],
             ]

class TicTacToeBoard:

    def __init__(self):
        self._cells = ['','','','','','','','','']
        #self._cells = ['']*9

    def get_cell(self,n):
        return self._cells[n]

    def make_move(self,n,token):
        """
        Place a token on the board

        :param n: cell from 0 to 8
        :param token: 'X', 'O'
        """

        assert token =='X' or token=='O'
        assert n>=0 and n<=8

        self._cells[n] = token

    def get_status(self):
        b = self._cells
        for w in WINS:
            x = b[w[0]]
            y = b[w[1]]
            z = b[w[2]]
            if (x == y and x == z and x=='X'):
                return 'X Wins'
            if (x == y and x == z and x == 'O'):
                return 'O Wins'
        for c in self._cells:
            if c=='':
                return 'Playing'
        return 'Tie'

