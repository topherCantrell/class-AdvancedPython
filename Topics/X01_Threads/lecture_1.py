# Sleep function causes current thread to pause

"""

https://github.com/topherCantrell/class-AdvancedPython

topherCantrell@gmail.com

"""
import time

def sleep_demo():
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(0.25)

import threading

def first_thread():
    
    def entry_function():
        while True:
            print('Here in entry_function')
            time.sleep(1)
        
    # t is an object that controls/monitors the thread        
    t = threading.Thread(target=entry_function,daemon=True)
    
    # Here the magic happens
    t.start()
    
    for i in range(5):
        print('In main')
        time.sleep(1)
        
def args_demo():
    def say_my_name(name,count):
        while count:
            print('I am',name,'count',count)
            count -= 1
            time.sleep(1)
    
    say_my_name('Topher',4)
            
    cnt = 1
    for n in ['bob','sue','jan','pat','tim']:
        tm = threading.Thread(target=say_my_name,args=(n,cnt))
        tm.start()
        cnt += 1

def stop_demo():
    running = True
    
    def entry_function():
        while running:
            print('I am running')
            time.sleep(1)
        print('I stopped running')
            
    tm = threading.Thread(target=entry_function)
    tm.start()
    time.sleep(5)
    running = False

def exclusion_demo():
    import sys
    
    a = 0
    b = 0
    
    my_lock = threading.Lock()
    
    def bump_a_b():
        global a,b
        while(True):
            with my_lock: # my_lock.acquire()
                a += 1
                b += 1
            # my_lock.release()
            my_lock.acquire()
            a += 1
            b += 1
            # Not here!
            if a!=b:
                print('What the heck?',a,b)
                sys.exit()
            my_lock.release()
    
    t1 = threading.Thread(target=bump_a_b)
    t1.start()
    
    t2 = threading.Thread(target=bump_a_b)
    t2.start()

def condition_demo():
    my_lock = threading.RLock()
    cv = threading.Condition(my_lock)
    
    name = ''
    def print_name():
        while True:
            my_lock.acquire()
            cv.wait()
            print('Name is',name)
            my_lock.release()
            
    tm = threading.Thread(target=print_name)
    tm.start()
            
    my_lock.acquire()
    name = 'Topher'
    cv.notify()
    my_lock.release()
    
    time.sleep(2)
    
    my_lock.acquire()
    name = 'Chris'
    cv.notify()
    my_lock.release()

print('hello')