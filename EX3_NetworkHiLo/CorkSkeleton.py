import socket
import TCPUtils

class CorkSkeleton(object):

    def __init__(self, corkServer):
        self.corkServer = corkServer        
        
    def mainLoop(self,port): 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind( ("", port))
        self.sock.listen(1)

        while True:
            conn, addr = self.sock.accept()            
            command = TCPUtils.readObject(conn)
            if(command=="postMessage"):
                self.corkServer.postMessage(TCPUtils.readObject())
            elif command=="getMessages":
                ms = self.corkServer.getMessages()
                TCPUtils.sendObject(conn,ms)
            elif command=="clearMessages":
                self.corkServer.clearMessages()
            else:
                pass # TODO
                
            conn.close()   
                        
    
      
    


