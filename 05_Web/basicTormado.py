import tornado.ioloop
import tornado.web
import os

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        #print(self.request)
        #print(str(self.request.headers))
        #print(self.request.headers["Accept-Language"])
        
        #self.set_status(987,"Oh Yeah")
        #self.set_header("My-Personal-Value","TOPHER")
        
        self.set_header("Content-Type","application/json")
        self.write('{"name":"chris", "numbers":[7,8,9]}')
        
    def post(self):
        #print(self.request)
        #print(str(self.request.headers))
        #print(self.request.headers["Content-Type"])
        
        print(self.request.arguments)
        
        print(self.request.body)
        
        self.write(self.get_argument("name")+" from "+self.get_argument("school"))
        
    def delete(self):
        self.write("DELETE requested")
        
class AnotherHandler(tornado.web.RequestHandler):
    def get(self):
        
        print(self.request)
        print(self.request.arguments)
        
        print(":"+self.get_argument("b")+":")
        print(":"+str(self.get_arguments("b"))+":")
        
        self.write("This is AnotherHandler")
        
        
class DecodeHandler(tornado.web.RequestHandler):
    def get(self,first,second):
        if (first=="chris"):
            self.write("Hi Chris ")
        self.write(":"+first+":"+second+":")

if __name__ == "__main__":
    
    # The directory of this module
    #root = os.path.dirname(__file__, "webroot")
    root = os.path.join(os.path.dirname(__file__), "webroot")
    
    handlers = [
        ("/my", MyHandler),
        ("/another", AnotherHandler),
        ("/complex/(.*)/(.*)", DecodeHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
        ]
    
    app = tornado.web.Application(handlers)
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()