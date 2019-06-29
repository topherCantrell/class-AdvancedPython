import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind( ("",1234) )
# sock.bind( ("localhost",1234) )

while True:
    data, addr = sock.recvfrom(1024)
    print "From:" + addr[0]+":"+str(addr[1])
    print "Got:" + data + ":"
    
    ret = data.upper()
    sock.sendto(ret,addr)
    
    data, addr = sock.recvfrom(1024)
    myData = pickle.loads(data)
    
    print repr(myData)