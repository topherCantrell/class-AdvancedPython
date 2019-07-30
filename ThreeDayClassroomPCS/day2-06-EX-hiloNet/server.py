import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind( ('',7777) )

sock.listen(1)

client,addr = sock.accept()

print('Got a connection!',addr)

import net_utils

s = net_utils.recv_string(client)
print('::'+s+'::')

