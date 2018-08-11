import tornado.ioloop
import tornado.web

import random

class HiLo(tornado.web.RequestHandler):
    
    myNumber = random.randrange(1,100) 
    
    def get(self):
        
        self.write("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hi Lo</title>
  </head>

  <body>
        """)
        
        guess = self.get_argument("guess", None)
        
        if not guess:
            self.write("<h1>Try to guess my number!</h1>")       
            # myNumber = random.randrange(1,100)            
            
        elif int(guess) > HiLo.myNumber:
            self.write("<h1>Lower</h1>")
            
        elif int(guess) < HiLo.myNumber:
            self.write("<h1>Higher</h1>")
            
        else:
            self.write("<h1>You got it!</h1>")       
            
        self.write("""        
  <form>
    Your guess: <input name="guess" autofocus> </br>
    <input type="submit">
  </form>
  
  <br>
  
  <a href="/hilo">Start new game</a>
  
  </body>
</html>
        """)
        
if __name__ == "__main__":
            
    handlers = [("/hilo", HiLo)]
    
    app = tornado.web.Application(handlers)
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()