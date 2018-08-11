import socket
from hilo import HiLo

# The client side (the proxy)

class UDPHiLo:
    
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)              
    
    def check_guess(self,guess):
        s = str(guess)
        self._sock.sendto(s.encode(),('localhost',2222))
        data, _ = self._sock.recvfrom(1000)
        return data.decode()

# The server side (the skeleton)
    
if __name__ == '__main__':
    
    game = HiLo()
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind( ('',2222) )  
    
    while True:
        
        data, addr = sock.recvfrom(1000)
        
        resp = game.check_guess(int(data))
        
        sock.sendto(resp.encode(), addr)
