# Primitive messages to send/receive all bytes from a byte array

def send_all_bytes(sock,msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

def read_all_bytes(sock,num):
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

def send_array_bytes(sock,data):
    slen = str(len(data))
    while len(slen)<8:
        slen = "0" + slen
    send_all(sock,slen.encode())
    send_all(sock,data)

def read_array_bytes(sock):
    slen = read_all_bytes(sock,8).decode()    
    return read_all_bytes(sock,int(slen))
            
# String are common ... use the array functions to send/read a string

def send_string(sock,msg):
    send_array_bytes(sock,msg.encode())
    
def read_string(sock):
    return read_array_bytes(sock).decode()

       
