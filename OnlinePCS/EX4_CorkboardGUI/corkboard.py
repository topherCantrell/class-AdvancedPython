# import datetime

class Message(object):

    def __init__(self, sender, message, date):
        # self._date = datetime.datetime.now()
        self._date = date
        self._sender = sender
        self._message = message
        
    def get_sender(self):
        return self._sender
    
    def get_message(self):
        return self._message
    
    def get_date(self):
        return self._date        
    
    def __repr__(self):
        return "Date:"+self.get_date()+" From:"+self.get_sender()+" Message:"+self.get_message()
        
class CorkBoard(object):

    def __init__(self):
        self._messages = []
    
    def post_message(self, message):
        self._messages.append(message)
    
    def clear(self):
        self._messages = []
    
    def get_messages(self):
        return self._messages
    
    def get_messages_from(self,filt):
        if(len(filt)==0 or len(filt[0])==0):
            return self.get_messages()        
        ret = []
        for m in self._messages:
            if(m.get_sender() in filt):
                ret.append(m)
        return ret
    
def make_example_data(board):
    message = Message("Chris","This is a test message","1/1/2018:08:45")
    board.post_message(message)
    message = Message("Pat","I see the test message","1/1/2018:09:00")
    board.post_message(message)
    message = Message("Bob","And so do I","1/2/2018:09:10")
    board.post_message(message)
        
if __name__ == '__main__':
    
    board = CorkBoard()
    
    make_example_data(board);  
    
    print(str(board.get_messages()))