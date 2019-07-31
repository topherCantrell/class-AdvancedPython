
import player
import random

class MrRandomPlayer(player.Player):
    
    def __init__(self,token):
        super().__init__(token,'Mr. Random')
        
    def get_move(self,board):
        empties = []
        for i in range(9):
            if board.get(i)=='':
                empties.append(i)
        return random.choice(empties)