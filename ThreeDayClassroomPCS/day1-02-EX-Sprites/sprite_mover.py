import sprites

import threading
import time

def entry_function():    
    id = sprites.make_rectangle(10,10)
    while True:        
        time.sleep(0.5)
        sprites.move_rectangle(id,4,2)        
        
sprites.make_gui()

tm = threading.Thread(target=entry_function) # args=(1,2,3,4)
tm.start()

sprites.run_gui()