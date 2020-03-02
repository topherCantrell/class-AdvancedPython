import Pyro4

@Pyro4.expose
class StringUtil(object):

    def __init__(self):
        pass
    
    def toUpperCase(self,s):
        return s.upper()
    
    def toLowerCase(self,s):
        return s.lower()
    
    def reverse(self,s):
        return s[::-1]
        