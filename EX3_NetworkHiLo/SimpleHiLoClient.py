#from hilo import HiLo
#game = HiLo()

#from hilo_udp import UDPHiLo
#game = UDPHiLo()

from hilo_tcp import TCPHiLo
game = TCPHiLo()

for x in range(1,101):
    
    resp = game.check_guess(x)
    
    print("Guess:"+str(x)+" Response:"+resp)
        
    if resp == "Correct":
        break
    