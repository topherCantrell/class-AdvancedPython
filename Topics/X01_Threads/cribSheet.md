# Threads

## Starting a Thread
```python
import threading

def entry_function():
    pass
    
tm = threading.Thread(target=entry_function)
tm.start()
```

