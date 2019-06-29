
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto("Hello World", ("localhost",1234))

data, addr = sock.recvfrom(1024)
print "From:" + addr[0]+":"+str(addr[1])
print "Got:" + data + ":"

myData = ["Hello","There",{"a":1234}]
sock.sendto(pickle.dumps(myData), ("localhost",1234))
