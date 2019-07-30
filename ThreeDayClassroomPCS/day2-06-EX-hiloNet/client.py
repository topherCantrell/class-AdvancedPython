import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('localhost',7777))

import net_utils

net_utils.send_string(sock,'Hello world')