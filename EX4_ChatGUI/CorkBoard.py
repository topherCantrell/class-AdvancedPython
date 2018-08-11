import Message

class CorkBoard(object):

    def __init__(self):
        self.messages = []
    
    def postMessage(self, message):
        self.messages.append(message)
    
    def clear(self):
        self.messages = []
    
    def getMessages(self):
        return self.messages
    
    def getMessagesFrom(self,filt):
        if(len(filt)==0):
            return self.getMessages()
        ret = []
        for m in self.messages:
            if(m.sender in filt):
                ret.append(m)
        return ret
    
def makeExampleData(board):
    message = Message.Message("Chris","This is a test message")
    board.postMessage(message)
    message = Message.Message("Pat","I see the test message")
    board.postMessage(message)
    message = Message.Message("Bob","And so do I")
    board.postMessage(message)
        
if __name__ == '__main__':
    
    board = CorkBoard()
    
    makeExampleData(board);  
    
    print(str(board.getMessages()))