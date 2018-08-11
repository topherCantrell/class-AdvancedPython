import tornado.ioloop
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    
    def get(self):
                        
        self.write("Cookies sent by browser:"+str(self.cookies)+"<br>")      
       
        cookieName = self.get_argument("name",None)
        cookieValue = self.get_argument("value","1234")
        cookieSecure = self.get_argument("secure",None)
        cookieClear = self.get_argument("clear",None)
        cookieDays = self.get_argument("days",None)
        
        if cookieDays:
            cookieDays = float(cookieDays)     
        
        if cookieClear:
            self.clear_cookie(cookieClear)
            self.write("Clearing cookie "+cookieClear+"<br>")   
                            
        if cookieName:   
            if cookieSecure:
                self.write("Setting secure cookie "+cookieName+"="+cookieValue+" days="+str(cookieDays))
                self.set_secure_cookie(cookieName,cookieValue,expires_days=cookieDays)                
            else:
                self.write("Setting cookie "+cookieName+"="+cookieValue+" days="+str(cookieDays))
                self.set_cookie(cookieName,cookieValue,expires_days=cookieDays)            

if __name__ == "__main__":
            
    handlers = [("/cook", MyHandler)]
    
    app = tornado.web.Application(handlers)
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()