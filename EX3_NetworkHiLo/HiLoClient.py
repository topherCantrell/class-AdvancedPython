import socket
import TCPUtils

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect( ("localhost",1234) )

start = 1
end = 100

while True:    
    guess = ((end - start) / 2) + start
    print guess
    
    lastGuess = guess    
    TCPUtils.sendString(client,str(guess))
    resp = TCPUtils.readString(client)
    
    if resp == "Higher":
        start = guess
    elif resp == "Lower":
        end = guess
    else:
        break
    
client.close()