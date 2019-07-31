
class Board:
    
    def __init__(self):
        self.clear()
        
    def clear(self):
        self._board = ['']*9
        
    def get(self,cell):
        return self._board[cell]
    
    def make_move(self,cell,token):
        self._board[cell] = token
        
    _wins = [
        [0,1,2],[3,4,5],[6,7,8], # Rows
        [0,3,6],[1,4,7],[2,5,8], # Columns
        [0,4,8],[2,4,6] # Diagonals
    ]
    
    def get_status(self):
        # Check for wins
        for trio in Board._wins:
            a = self.get(trio[0])
            b = self.get(trio[1])
            c = self.get(trio[2])
            if a==b and a==c and a!='':
                return a
        # Check for empty cell
        for i in range(9):
            if self.get(i)=='':
                return 'Play'
        # Must be a tie
        return 'Tie'       
    
    def __str__(self):
        ret = ''
        for i in range(9):
            c = self.get(i)
            if c=='':
                c='.'
            ret = ret + c
            if i==2 or i==5 or i==8:
                ret = ret + '\n'
        return ret
                    