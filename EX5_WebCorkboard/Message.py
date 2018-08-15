import datetime

class Message(object):

    def __init__(self, sender, message):
        self.date = datetime.datetime.now()
        self.sender = sender
        self.message = message
        
    
    def __repr__(self):
        return "Date:"+self.date.strftime("%Y-%m-%d %H:%M")+" From:"+self.sender+" Message:"+self.message;
        