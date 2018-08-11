import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 80)
sock.bind(server_address)
sock.listen(1)

while True:
    try:
        print 'waiting for a connection'
        connection, client_address = sock.accept()        
        print 'connection from', client_address
        
        # Read the request from the server
        data = connection.recv(1024)
        print ":"+data+":"
        
        # Send back a response
        connection.sendall("HTTP/1.0 200 OK\nAccess-Control-Allow-Origin: null\n\n99")               
    
    finally:
        connection.close()


