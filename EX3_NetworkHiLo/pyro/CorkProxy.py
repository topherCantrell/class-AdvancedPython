import socket
import TCPUtils

class CorkProxy(object):

    def __init__(self, address, port):
        self.address = address
        self.port = port
    
    def postMessage(self, message):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        sock.connect( (self.address, self.port))
        TCPUtils.sendObject(sock,"postMessage")
        TCPUtils.sendObject(sock,message)
        sock.close()        
            
    def getMessages(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        sock.connect( (self.address, self.port))
        TCPUtils.sendObject(sock,"getMessages")
        messages = TCPUtils.readObject(sock)
        sock.close()
        return messages     
            
    def clearMessages(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        sock.connect( (self.address, self.port))
        TCPUtils.sendObject(sock,"clearMessages")
        sock.close()     