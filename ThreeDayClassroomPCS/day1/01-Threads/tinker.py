
import time
import threading

running = True

def print_hello():
    while running:
        print('Hello')
        time.sleep(1)
        
def print_world():
    while running:
        print('World')
        time.sleep(2)
        
threading.Thread(target=print_hello).start()
threading.Thread(target=print_world).start()

       
    

print('End of main')
