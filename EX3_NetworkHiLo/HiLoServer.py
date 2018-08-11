import socket
import random
import TCPUtils

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind( ("", 1234))
server.listen(1)

client, addr = server.accept()
print 'Connection address:', addr

number = random.randint(1,101)
print "My number is ",number

while True:
    print "Waiting for guess"
    guess = TCPUtils.readString(client)

    clientGuess = int(guess)
    print "Guess is ",guess

    if clientGuess < number:
        TCPUtils.sendString(client,"Higher")
        print "Higher"
        
    elif clientGuess > number:
        TCPUtils.sendString(client,"Lower")
        print "Lower"
        
    else:
        TCPUtils.sendString(client,"You guessed it")
        print "Got it"
        break
    
print "Ending"
    
client.close()
server.close()
     

