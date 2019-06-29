import socket
from hilo import HiLo

import tcputils

# The client side (proxy)

class TCPHiLo:
    
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._sock.connect( ('localhost',3333) )
    
    def check_guess(self,guess):        
        tcputils.send_string(self._sock,str(guess))
        return tcputils.read_string(self._sock)
    
        #tcputils.send_object(self._sock,guess)
        #return tcputils.read_object(self._sock)


# The server side (skeleton)

if __name__ == '__main__':
    
    game = HiLo()
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind( ('',3333) )
    sock.listen(1)
    
    c,_ = sock.accept()
    
    while True:
        
        guess = tcputils.read_string(c)        
        resp = game.check_guess(int(guess))        
        tcputils.send_string(c, resp)
        
        #guess = tcputils.read_object(c)
        #resp = game.check_guess(guess)
        #tcputils.send_object(c,resp)
