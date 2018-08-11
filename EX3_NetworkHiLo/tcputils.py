import pickle

# Primitive messages to send/receive all bytes from a byte array

def send_all(sock,msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

def read_all(sock,num):
    chunks = []
    bytes_recd = 0
    while bytes_recd < num:
        chunk = sock.recv(min(num - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return b''.join(chunks)

# Send and read an arbitrary array of bytes (the length goes first)

def send_array(sock,data):
    slen = str(len(data))
    while len(slen)<8:
        slen = "0" + slen
    send_all(sock,slen.encode())
    send_all(sock,data)

def read_array(sock):
    slen = read_all(sock,8).decode()    
    return read_all(sock,int(slen))
            
# String are common ... use the array functions to send/read a string

def send_string(sock,msg):
    send_array(sock,msg.encode())
    
def read_string(sock):
    return read_array(sock).decode()

# Use the array functions to send/read pickled objects

def read_object(sock):
    dataString = read_array(sock)
    return pickle.loads(dataString)

def send_object(sock,obj):
    dataString = pickle.dumps(obj)
    send_array(sock,dataString)
        
