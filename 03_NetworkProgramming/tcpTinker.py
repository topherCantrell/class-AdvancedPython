import socket

import TCPUtils

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)

s.connect( ("localhost", 8888))

TCPUtils.sendObject(s,["true",True,1.1])


