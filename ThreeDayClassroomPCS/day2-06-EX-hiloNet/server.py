import socket
import random
import net_utils

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind( ('',7777) )

sock.listen(1)

while True:
    
    print('Waiting on connection')
    client,addr = sock.accept()
    print('Serving',addr)
    
    my_number = random.randint(1,101)
    
    while True:
        
        guess = net_utils.recv_string(client)
        guess = int(guess)
        
        if guess < my_number:
            net_utils.send_string(client,'Higher!')
        if guess > my_number:
            net_utils.send_string(client,'Lower!')
        if guess == my_number:
            net_utils.send_string(client,'You got it!')
            client.close()
            break
            


