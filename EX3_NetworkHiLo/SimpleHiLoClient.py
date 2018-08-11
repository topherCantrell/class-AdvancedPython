import socket
import TCPUtils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect( ("localhost",1234) )

for x in range(1,101):
    TCPUtils.sendString(client,str(x))
    resp = TCPUtils.readString(client)
    print x, resp
    if resp == "You guessed it":
        break
    
client.close()