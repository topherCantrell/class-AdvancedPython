
def send_all(sock,msg):
    num_sent = 0
    while num_sent<len(msg):
        n = sock.send(msg[num_sent:].encode())
        if n==0:
            raise Exception("Socket Closed Send")
        num_sent = num_sent + n    

def recv_all(sock,num):
    num_read = 0
    ret = ''
    while len(ret)<num:
        n = sock.recv(num-len(ret))
        if n==0:
            raise Exception("Socket Closed Read")
        ret = ret + n.decode()
    return ret

def send_string(sock,s):
    t = str(len(s))
    while(len(t)<8):
        t = '0'+t
    send_all(sock,t)
    send_all(sock,s)

def recv_string(sock):
    t = int(recv_all(sock,8))
    return recv_all(sock,t)
