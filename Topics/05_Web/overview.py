import socket

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', 80)
    sock.bind(server_address)
    sock.listen(1)
    
    while True:
        try:
            print('waiting for a connection')
            connection, client_address = sock.accept()        
            print('connection from '+repr(client_address))
            
            # Read the request from the server
            data = connection.recv(1024)
            print(":"+data.decode()+":")
            
            # Send back a response
            connection.sendall(b"HTTP/1.0 200 OK\n\nHello World")               
        
        finally:
            connection.close()

def browser():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('google.com', 80)
    sock.connect(address)
    
    sock.sendall(b"GET / HTTP/1.0\n\n")
    
    data = sock.recv(1000)
    print(":"+data.decode()+":")
            
    sock.close()

#server()
browser()