import pickle

def readObject(sock):
    dataString = readString(sock)
    return pickle.loads(dataString)

def sendObject(sock,obj):
    dataString = pickle.dumps(obj)
    sendString(sock,dataString)
        
def sendString(sock,msg):
    slen = str(len(msg))
    while len(slen)<8:
        slen = "0" + slen
    sendAll(sock,slen)
    sendAll(sock,msg)
    
def readString(sock):
    slen = readAll(sock,8)
    return readAll(sock,int(slen))
            
def sendAll(sock,msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

def readAll(sock,num):
    chunks = []
    bytes_recd = 0
    while bytes_recd < num:
        chunk = sock.recv(min(num - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)
