import tornado.ioloop
import tornado.web

"""
cookie = sid (auto increment integer starting at 10000)

?user=ccantrell&pass=password   Login
?logout                         Logout

Nothing ... count or deny

"""

class SessionPlay(tornado.web.RequestHandler):
    
    sessions = {}
    next_id = 10000
   
    def get(self):
        
        logout = self.get_argument("logout",None)
        user = self.get_argument("user",None)
        password = self.get_argument("pass",None)
        
        sid = self.get_cookie("sid",None)
        
        if logout and sid:
            self.clear_cookie("sid")
            del SessionPlay.sessions[sid]
            self.write("Logged out")
            return
        
        if user:
            session = {"user":user, "password":password, "count":1}
            sid = str(SessionPlay.next_id)
            SessionPlay.next_id += 1
            SessionPlay.sessions[sid] = session
            self.set_cookie("sid",sid)            
            self.write("Logged in")
            return
                
        if not sid:
            self.write("I don't know you (you have no cookie)")
            return
        
        if not sid in SessionPlay.sessions:
            self.write("I don't know you (unknown sid)")
            self.clear_cookie("sid")
            return
        
        session = SessionPlay.sessions[sid]
        session["count"] += 1
        self.write(str(session))        

if __name__ == "__main__":    
        
    handlers = [
        ("/session", SessionPlay)        
        ]
    
    app = tornado.web.Application(handlers)
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()        