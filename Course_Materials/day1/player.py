
class Player:
            
    def __init__(self,token,name):
        self._token = token
        self._name = name
    
    def get_token(self):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def get_token(self):
        return self._token
    
    def get_move(self,board):
        # Override me
        pass
