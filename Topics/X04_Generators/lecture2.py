
class _TTBI:
    def __init__(self,cells):
        self._cells = cells
        self._pos = 0
        
    def __next__(self):
        if self._pos>= len(self._cells):
            raise StopIteration
        else:            
            ret = self._cells[self._pos]
            self._pos += 1
            return ret
            

class TicTacToeBoard:
    
    def __init__(self): # Could pass in range here
        self._cells = ['A','B','C','D','E','F','G','H','I']
        
    # Other methods here
    
    def __iter__(self):
        return _TTBI(self._cells)
        
        
ttt = TicTacToeBoard()

i = ttt.__iter__()
i = iter(ttt)

print(i.__next__())
print(next(i))

for c in ttt:
    print(c)
    