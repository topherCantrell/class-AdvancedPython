import socket

import TCPUtils

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)

s.bind( ("", 8888))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)

d = TCPUtils.readObject(conn)

print d