import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('localhost',7777))

import net_utils

while True:
    g = input('Guess: ')
    net_utils.send_string(sock,g)
    resp = net_utils.recv_string(sock)
    print(resp)
    if(resp.startswith('You got')):
        break
