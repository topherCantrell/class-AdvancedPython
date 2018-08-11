class NameKeeper(object):

    def __init__(self):
        self.name = "Chris Cantrell"
            
    def get_name(self):        
        return("Chris Cantrell")
    
    
n = NameKeeper()

me = n.name
me = n.get_name()
print(me)

class NameKeepers(object):
    "Stuff"
    
n = NameKeeper()

n.name = "Hello"
print(n.name)