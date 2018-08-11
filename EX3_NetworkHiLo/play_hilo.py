#from hilo import HiLo
#game = HiLo()

#from hilo_udp import UDPHiLo
#game = UDPHiLo()

from hilo_tcp import TCPHiLo
game = TCPHiLo()

while True:
    
    guess = input('What is your guess? ')
    
    resp = game.check_guess(int(guess))
    
    print(resp)
    
    if resp=='Correct':
        break