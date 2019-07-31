
import player

class HumanPlayer(player.Player):
    
    def __init__(self,token,name):
        super().__init__(token,name)
        
    def get_move(self,board):
        # TODO make sure move is valid
        move = input('Your move '+self.get_name()+': ')
        return int(move)