import threading
import time

import sprites


def horiz():
    id = sprites.make_rectangle(10,10)
    while True:
        for _ in range(50):
            time.sleep(0.25)
            sprites.move(id,5,0)
        for _ in range(50):
            time.sleep(0.25)
            sprites.move(id,-5,0)

def entry_function():    
    id = sprites.make_rectangle(10,10)
    while True:        
        time.sleep(0.5)
        sprites.move(id,4,2)        
        
sprites.make_gui()

tm = threading.Thread(target=entry_function) # args=(1,2,3,4)
tm.start()

threading.Thread(target=horiz).start()

sprites.run_gui()