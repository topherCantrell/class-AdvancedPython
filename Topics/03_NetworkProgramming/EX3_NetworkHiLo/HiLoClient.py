#from hilo import HiLo
#game = HiLo()

#from hilo_udp import UDPHiLo
#game = UDPHiLo()

from hilo_tcp import TCPHiLo
game = TCPHiLo()

start = 1
end = 100

while True:    
    guess = ((end - start) / 2) + start
    guess = int(guess)
    
    lastGuess = guess    
    
    resp = game.check_guess(guess)
    
    print("Guess:"+str(guess)+" Response:"+resp)
            
    if resp == "Higher":
        start = guess
    elif resp == "Lower":
        end = guess
    else:
        break
    