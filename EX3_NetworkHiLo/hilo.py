import random

class HiLo:
    
    def __init__(self):
        self.new_game()

    def check_guess(self,guess):
        if guess > self._my_number:
            return "Lower"
        
        if guess < self._my_number:
            return "Higher"
        
        return "Correct"
    
    def new_game(self):
        self._my_number = random.randint(1,101)