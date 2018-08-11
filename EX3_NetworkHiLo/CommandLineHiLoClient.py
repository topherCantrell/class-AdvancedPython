import socket
import TCPUtils

client = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM)

client.connect( ("localhost",1234) )

print "The server is thinking of a number between 1 and 100."
print "Try and guess it!"
print ""

while True:
    guess = raw_input("Your guess: ")
    TCPUtils.sendString(client,guess)
    resp = TCPUtils.readString(client)
    print "Server says: ", resp
    if resp == "You guessed it":
        break
    
client.close()