import tornado.ioloop
import tornado.web

import corkboard 

board = corkboard.CorkBoard()     
corkboard.make_example_data(board)

class ChatHandler(tornado.web.RequestHandler):    
           
    def get(self):
        
        sender = self.get_argument("sender",None)
        message = self.get_argument("message",None)
        # filter = self.get_argument("filter",None)
        # clear = self.get_argument("clear",None)
        
        if (sender and message):
            m = corkboard.Message(sender,message,"NOW")
            board.post_message(m)       
         
        # We'll send this back as a shortcut   
        if not sender:
            sender = ''     
            
        self.write(
"""
<html>

    <H1>Web Chat</H1>

    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>

    <table>
    <tr>
        <th>Date</th>
        <th>Sender</th>
        <th>Message</th>
    </tr>
""")
        
        for post in board.get_messages():
            self.write("<tr><td>"+post.get_date()+"</td><td>"+post.get_sender()+"</td><td>"+post.get_message()+"</td></tr>")            
            
        self.write(
"""  
    </table>

    <hr>

    <form action="chat">
        Filter: <input type="text" name="filter">
        <input type="checkbox" name="clear">Clear Messages
        <p>
        Sender: <input type="text" name="sender" value='"""+sender+"""'>
        Message: <input type="text" name="message">
        <input type="Submit">
    </form>

</html>
""")          

if __name__ == "__main__":

    # http://localhost/chat?sender=Chris&date=10/8/2017&message=anybody%20out%20there?
            
    handlers = [
        ("/chat", ChatHandler)
    ]
    
    app = tornado.web.Application(handlers)
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()